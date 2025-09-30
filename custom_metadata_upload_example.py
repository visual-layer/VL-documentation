#!/usr/bin/env python3
"""
Custom Metadata Upload Example Script for Visual Layer
=====================================================

This script demonstrates how to upload custom metadata to Visual Layer using:
1. A CSV file containing your metadata
2. A metadata.json file exported from Visual Layer (provides filename-to-media_id mapping)

This is a SPECIFIC USE CASE example script. Users can modify the field detection
logic to match their specific needs. For advanced use cases, custom metadata
deletion, or additional support, contact Visual Layer support.

Requirements:
- Visual Layer on-premises installation (no authentication required)
- metadata.json file exported from Visual Layer dataset
- CSV file with metadata and filename column

Usage:
    python custom_metadata_upload_example.py metadata.csv metadata.json \
        --dataset-id=your-dataset-id --base-url=http://localhost:8080
"""

import csv
import json
import requests
import argparse
import os
import pandas as pd
import time
from typing import Dict, List, Any, Optional

class CustomMetadataUploader:
    """
    Example uploader for Visual Layer custom metadata.

    This demonstrates the basic API workflow:
    1. Read CSV metadata and JSON export file
    2. Create filename-to-media_id mapping
    3. Analyze CSV fields and detect data types
    4. Create custom fields via API
    5. Upload metadata values for each field
    6. Monitor upload progress
    """

    def __init__(self, dataset_id: str, base_url: str):
        self.dataset_id = dataset_id
        self.raw_base_url = base_url.rstrip('/')

        # Automatically add /api/v1/datasets if not present
        if not base_url.endswith('/api/v1/datasets'):
            if base_url.endswith('/'):
                base_url = base_url.rstrip('/')
            self.base_url = f"{base_url}/api/v1/datasets"
        else:
            self.base_url = base_url

        # Create HTTP session (no authentication for on-prem)
        self.session = requests.Session()
        self._temp_files = []  # Track temporary files for cleanup

    def read_csv_metadata(self, csv_file: str) -> List[Dict[str, Any]]:
        """
        Read CSV file containing metadata.

        Expected format:
        filename,field1,field2,field3,...
        image1.jpg,value1,value2,value3,...
        image2.jpg,value1,value2,value3,...
        """
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"CSV file not found: {csv_file}")

        print(f"📊 Reading CSV metadata from: {csv_file}")
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        print(f"   ✅ Loaded {len(data)} records")
        return data

    def read_metadata_json(self, json_file: str) -> List[Dict[str, Any]]:
        """
        Read metadata.json file exported from Visual Layer.

        This file contains the mapping from filenames to media_ids that Visual Layer
        uses internally. You get this file by exporting your dataset from Visual Layer.
        """
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"Metadata JSON file not found: {json_file}")

        print(f"🗂️  Reading Visual Layer export from: {json_file}")
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Handle different export formats
        if isinstance(data, list):
            media_items = data
        elif isinstance(data, dict) and 'media_items' in data:
            media_items = data['media_items']
        else:
            raise ValueError("Unknown metadata.json format - expected list or dict with 'media_items'")

        print(f"   ✅ Loaded {len(media_items)} media items")
        return media_items

    def create_filename_mapping(self, media_items: List[Dict[str, Any]]) -> Dict[str, str]:
        """
        Create mapping from filename to media_id.

        This maps the filenames in your CSV to the media_ids that Visual Layer
        uses internally. The media_ids come from the exported metadata.json file.
        """
        print("🔍 Creating filename-to-media_id mapping...")

        mapping = {}
        for item in media_items:
            media_id = item.get('media_id')
            file_name = item.get('file_name', '')

            if media_id and file_name:
                # Use just the filename without path for matching
                basename = os.path.basename(file_name)
                mapping[basename] = media_id

        print(f"   ✅ Created mapping for {len(mapping)} files")
        return mapping

    def analyze_csv_fields(self, csv_data: List[Dict[str, Any]]) -> Dict[str, str]:
        """
        Analyze CSV fields and automatically detect data types.

        This is where you can customize the field detection logic for your use case.
        Currently detects: string, float, datetime, enum

        You can modify this function to:
        - Skip certain fields
        - Force specific fields to certain types
        - Add custom detection logic for your data
        """
        if not csv_data:
            return {}

        print("🔍 Analyzing CSV fields...")
        field_types = {}
        sample_row = csv_data[0]

        # Skip the filename field - it's used for mapping, not as metadata
        skip_fields = {'filename', 'file_name', 'image_filename'}

        for field_name, value in sample_row.items():
            if field_name in skip_fields:
                continue

            # Detect field type based on sample values
            if self._is_float(value):
                field_types[field_name] = 'float'
            elif self._is_datetime(value):
                field_types[field_name] = 'datetime'
            elif self._looks_like_enum(field_name, csv_data):
                field_types[field_name] = 'enum'
            else:
                # Default to string for everything else
                field_types[field_name] = 'string'

        print("   📋 Field analysis results:")
        for field_name, field_type in field_types.items():
            print(f"      {field_name}: {field_type}")

        return field_types

    def _is_float(self, value: str) -> bool:
        """Check if value looks like a floating point number."""
        if not isinstance(value, str) or not value.strip():
            return False
        try:
            float(value)
            return '.' in value or 'e' in value.lower()
        except (ValueError, TypeError):
            return False

    def _is_datetime(self, value: str) -> bool:
        """Check if value looks like a date/time using pandas parsing."""
        if not isinstance(value, str) or not value.strip():
            return False

        try:
            pd.to_datetime(value.strip())
            return True
        except (ValueError, TypeError, pd.errors.ParserError):
            return False

    def _looks_like_enum(self, field_name: str, csv_data: List[Dict[str, Any]]) -> bool:
        """
        Check if field looks like it should be an enum (categorical data).

        This is a simple heuristic - you can customize this logic for your data.
        """
        unique_values = set()
        sample_size = min(50, len(csv_data))  # Check first 50 rows

        for row in csv_data[:sample_size]:
            val = str(row.get(field_name, '')).strip()
            if val:
                unique_values.add(val)

        # If we have few unique values relative to total, might be enum
        # This is just an example heuristic - adjust for your data
        if len(unique_values) <= 10 and len(unique_values) < sample_size * 0.5:
            return True

        return False

    def create_custom_field(self, field_name: str, field_type: str, enum_values: List[str] = None) -> Optional[str]:
        """
        Create a custom metadata field in Visual Layer.

        Returns the task_id if successful, None if field already exists or creation fails.
        """
        print(f"🔧 Creating custom field: {field_name} ({field_type})")

        # Prepare field definition
        field_data = {
            "field_name": field_name,
            "field_type": field_type
        }

        # Add enum options if this is an enum field
        if field_type == 'enum' and enum_values:
            unique_values = list(set(enum_values))[:20]  # API limit is 20 enum values
            field_data["enum_options"] = unique_values
            field_data["is_multi"] = False  # Single-select enum
            print(f"   📝 Adding {len(unique_values)} enum options")

        # Make API request to create field
        url = f"{self.base_url}/{self.dataset_id}/custom_metadata/tasks"

        try:
            response = self.session.post(url, json=field_data)
            if response.status_code == 200:
                result = response.json()
                task_id = result.get('task_id')
                print(f"   ✅ Created field with task ID: {task_id}")
                return task_id
            elif "already exists" in response.text.lower():
                print(f"   🔄 Field already exists, skipping creation")
                return None
            else:
                print(f"   ❌ Failed to create field: {response.status_code} - {response.text}")
                return None
        except requests.RequestException as e:
            print(f"   ❌ Request failed: {str(e)}")
            return None

    def upload_field_data(self, task_id: str, field_name: str, field_type: str,
                         csv_data: List[Dict[str, Any]], filename_mapping: Dict[str, str]) -> bool:
        """
        Upload metadata values for a specific field.

        This creates the JSON payload and uploads it to Visual Layer.
        """
        print(f"   📤 Preparing upload data for field: {field_name}")

        upload_data = []
        matched_count = 0

        # Process each CSV row
        for row in csv_data:
            # Find the filename in the row (flexible field name matching)
            filename = None
            for field in ['filename', 'file_name', 'image_filename']:
                if field in row and row[field]:
                    filename = os.path.basename(row[field].strip())
                    break

            if not filename:
                continue

            # Look up the Visual Layer media_id for this filename
            media_id = filename_mapping.get(filename)
            if not media_id:
                continue  # Skip files not found in Visual Layer

            # Get the metadata value for this field
            value = row.get(field_name, '')
            if not value:
                continue  # Skip empty values

            # Convert value to appropriate type
            converted_value = self._convert_value(value, field_type)
            if converted_value is not None:
                upload_data.append({
                    "media_id": media_id,
                    "value": converted_value
                })
                matched_count += 1

        print(f"   📊 Prepared {len(upload_data)} upload entries from {len(csv_data)} CSV rows")

        if not upload_data:
            print(f"   ⚠️  No data to upload for field {field_name}")
            return False

        # Save upload data to temporary JSON file
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(upload_data, f, indent=2)
            temp_file = f.name

        self._temp_files.append(temp_file)

        # Upload the file
        url = f"{self.base_url}/{self.dataset_id}/custom_metadata/tasks/{task_id}"

        try:
            with open(temp_file, 'rb') as f:
                files = {'file': (f'metadata_{field_name}.json', f, 'application/json')}
                response = self.session.post(url, files=files)

            if response.status_code in [200, 202]:
                print(f"   ✅ Upload completed successfully")
                return True
            else:
                print(f"   ❌ Upload failed: {response.status_code} - {response.text}")
                return False

        except requests.RequestException as e:
            print(f"   ❌ Upload request failed: {str(e)}")
            return False

    def _convert_value(self, value: str, field_type: str) -> Any:
        """Convert string value to appropriate type for Visual Layer API."""
        if not value or not isinstance(value, str):
            return None

        value = value.strip()
        if not value:
            return None

        try:
            if field_type == 'float':
                return float(value)
            elif field_type == 'datetime':
                # Convert to ISO 8601 format
                dt = pd.to_datetime(value)
                if dt.tz is None:
                    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')
                else:
                    return dt.tz_convert('UTC').strftime('%Y-%m-%dT%H:%M:%SZ')
            else:
                # string and enum types
                return value
        except (ValueError, TypeError, pd.errors.ParserError):
            print(f"   ⚠️  Could not convert value '{value}' to {field_type}")
            return None

    def check_upload_status(self, task_id: str) -> str:
        """Check the status of an upload task."""
        url = f"{self.base_url}/{self.dataset_id}/custom_metadata/tasks/{task_id}/status"

        try:
            response = self.session.get(url)
            if response.status_code == 200:
                result = response.json()
                status = result.get('status', 'unknown')

                if status == 'COMPLETED':
                    inserted_rows = result.get('inserted_rows', 0)
                    print(f"   ✅ Upload completed: {inserted_rows} rows inserted")
                elif status == 'COMPLETED_WITH_ERRORS':
                    error_count = result.get('error_count', 0)
                    inserted_rows = result.get('inserted_rows', 0)
                    print(f"   ⚠️  Upload completed with {error_count} errors, {inserted_rows} rows inserted")

                return status
            else:
                return 'error'
        except requests.RequestException:
            return 'error'

    def wait_for_upload_completion(self, task_id: str, field_name: str) -> str:
        """Wait for upload to complete by polling the status endpoint."""
        print(f"   ⏳ Waiting for upload completion...")

        while True:
            status = self.check_upload_status(task_id)

            if status in ['COMPLETED', 'COMPLETED_WITH_ERRORS']:
                return status
            elif status == 'error':
                print(f"   ❌ Error checking upload status")
                return 'error'
            elif status == 'IN_PROGRESS':
                print(f"   📊 Upload in progress...")
            else:
                print(f"   📋 Status: {status}")

            time.sleep(3)  # Check every 3 seconds

    def cleanup_temp_files(self):
        """Clean up temporary files created during processing."""
        for temp_file in self._temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except OSError:
                pass  # Ignore cleanup errors

    def upload_metadata(self, csv_file: str, json_file: str):
        """
        Main workflow to upload custom metadata.

        This demonstrates the complete process:
        1. Read CSV and JSON files
        2. Create filename mapping
        3. Analyze fields and detect types
        4. Create custom fields in Visual Layer
        5. Upload metadata for each field
        6. Wait for completion
        """
        try:
            print("🚀 Starting Custom Metadata Upload")
            print(f"📁 CSV file: {csv_file}")
            print(f"🗂️  JSON file: {json_file}")
            print(f"🎯 Dataset ID: {self.dataset_id}")
            print(f"🌐 Base URL: {self.raw_base_url}")

            # Step 1: Read input files
            csv_data = self.read_csv_metadata(csv_file)
            media_items = self.read_metadata_json(json_file)

            # Step 2: Create filename mapping
            filename_mapping = self.create_filename_mapping(media_items)
            if not filename_mapping:
                raise ValueError("No filename mappings created - check that your CSV filenames match the exported JSON")

            # Step 3: Analyze CSV fields
            field_types = self.analyze_csv_fields(csv_data)
            if not field_types:
                raise ValueError("No metadata fields found in CSV")

            print(f"\n🎯 Processing {len(field_types)} metadata fields...")

            # Step 4: Process each field
            successful_uploads = 0
            for field_name, field_type in field_types.items():
                print(f"\n🔄 Processing field: {field_name} ({field_type})")

                try:
                    # Collect enum values if needed
                    enum_values = []
                    if field_type == 'enum':
                        enum_values = [str(row[field_name]).strip() for row in csv_data
                                     if row.get(field_name, '').strip()]

                    # Create the custom field
                    task_id = self.create_custom_field(field_name, field_type, enum_values)
                    if not task_id:
                        print(f"   ⏭️  Skipping field {field_name}")
                        continue

                    # Upload the data
                    if self.upload_field_data(task_id, field_name, field_type, csv_data, filename_mapping):
                        # Wait for completion
                        final_status = self.wait_for_upload_completion(task_id, field_name)
                        if final_status in ['COMPLETED', 'COMPLETED_WITH_ERRORS']:
                            successful_uploads += 1
                            status_icon = "✅" if final_status == 'COMPLETED' else "⚠️"
                            print(f"   {status_icon} Field {field_name} upload {final_status.lower()}")
                        else:
                            print(f"   ❌ Field {field_name} upload failed")
                    else:
                        print(f"   ❌ Failed to upload data for field {field_name}")

                except Exception as e:
                    print(f"   ❌ Error processing field {field_name}: {str(e)}")
                    continue

            print(f"\n🎉 Upload process completed!")
            print(f"✅ Successfully uploaded {successful_uploads} out of {len(field_types)} fields")

            if successful_uploads > 0:
                print(f"\n💡 Your custom metadata fields are now available in Visual Layer!")
                print(f"   You can use them for filtering and searching in the UI.")

        finally:
            # Always clean up temporary files
            self.cleanup_temp_files()

def main():
    parser = argparse.ArgumentParser(
        description='Upload custom metadata to Visual Layer (On-Premises)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python custom_metadata_upload_example.py metadata.csv metadata.json \\
    --dataset-id=abc123 --base-url=http://localhost:2080

Required Files:
  metadata.csv    - Your metadata with filename column
  metadata.json   - Export from Visual Layer (provides filename-to-media_id mapping)

Note: This script is designed for on-premises Visual Layer installations.
For cloud deployments or advanced use cases, contact Visual Layer support.
        """
    )

    parser.add_argument('csv_file', help='Path to CSV file containing metadata')
    parser.add_argument('json_file', help='Path to metadata.json file exported from Visual Layer')
    parser.add_argument('--dataset-id', required=True, help='Visual Layer dataset ID')
    parser.add_argument('--base-url', default='http://localhost:2080',
                       help='Visual Layer base URL (default: http://localhost:2080)')

    args = parser.parse_args()

    # Create uploader and run the workflow
    uploader = CustomMetadataUploader(args.dataset_id, args.base_url)
    uploader.upload_metadata(args.csv_file, args.json_file)

if __name__ == "__main__":
    main()