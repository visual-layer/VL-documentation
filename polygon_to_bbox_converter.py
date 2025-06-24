#!/usr/bin/env python3
"""
Polygon to Bounding Box Converter

This script converts polygon annotations from JSON files to Visual Layer bounding box CSV format.
It processes JSON files containing polygon annotations and generates a CSV file with bounding boxes.

Usage:
    python polygon_to_bbox_converter.py [input_directory] [output_csv]

Example:
    python polygon_to_bbox_converter.py boj/ annotations.csv
"""

import json
import csv
import os
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any


def extract_polygon_points(shape: Dict[str, Any]) -> List[Tuple[int, int]]:
    """
    Extract polygon points from a shape annotation.
    
    Args:
        shape: Dictionary containing shape information with 'points' key
        
    Returns:
        List of (x, y) coordinate tuples
    """
    if 'points' not in shape:
        return []
    
    points = []
    for point in shape['points']:
        if len(point) >= 2:
            x, y = int(point[0]), int(point[1])
            points.append((x, y))
    
    return points


def polygon_to_bbox(points: List[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    """
    Convert polygon points to bounding box coordinates.
    
    Args:
        points: List of (x, y) coordinate tuples defining the polygon
        
    Returns:
        Tuple of (col_x, row_y, width, height) for bounding box
        - col_x: Left x-coordinate
        - row_y: Top y-coordinate  
        - width: Width of bounding box
        - height: Height of bounding box
    """
    if not points:
        return (0, 0, 0, 0)
    
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    
    col_x = min_x
    row_y = min_y
    width = max_x - min_x
    height = max_y - min_y
    
    return (col_x, row_y, width, height)


def process_json_file(json_path: Path) -> List[Dict[str, Any]]:
    """
    Process a JSON annotation file and extract bounding boxes.
    
    Args:
        json_path: Path to the JSON annotation file
        
    Returns:
        List of dictionaries containing bounding box information
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error reading {json_path}: {e}")
        return []
    
    if 'shapes' not in data:
        print(f"No 'shapes' key found in {json_path}")
        return []
    
    # Get the corresponding image filename
    image_filename = data.get('imagePath', json_path.stem + '.png')
    
    bboxes = []
    for shape in data['shapes']:
        if shape.get('shape_type') != 'polygon':
            continue
            
        label = shape.get('label', 'unknown')
        points = extract_polygon_points(shape)
        
        if not points:
            continue
            
        col_x, row_y, width, height = polygon_to_bbox(points)
        
        # Skip invalid bounding boxes (zero width or height)
        if width <= 0 or height <= 0:
            continue
            
        bbox_info = {
            'filename': image_filename,
            'col_x': col_x,
            'row_y': row_y,
            'width': width,
            'height': height,
            'label': label
        }
        bboxes.append(bbox_info)
    
    return bboxes


def convert_directory_to_csv(input_dir: Path, output_csv: Path):
    """
    Convert all JSON annotation files in a directory to a single CSV file.
    
    Args:
        input_dir: Directory containing JSON annotation files
        output_csv: Output CSV file path
    """
    if not input_dir.exists():
        print(f"Input directory {input_dir} does not exist")
        return
    
    # Find all JSON files in the directory  
    json_files = list(input_dir.glob('*.json'))
    
    if not json_files:
        print(f"No JSON files found in {input_dir}")
        return
    
    print(f"Found {len(json_files)} JSON files to process")
    
    all_bboxes = []
    
    # Process each JSON file
    for json_file in json_files:
        print(f"Processing: {json_file.name}")
        bboxes = process_json_file(json_file)
        all_bboxes.extend(bboxes)
        print(f"  Found {len(bboxes)} bounding boxes")
    
    # Write to CSV
    if all_bboxes:
        write_bboxes_to_csv(all_bboxes, output_csv)
        print(f"\nConversion complete! Output saved to: {output_csv}")
        print(f"Total bounding boxes: {len(all_bboxes)}")
    else:
        print("No bounding boxes found to export")


def write_bboxes_to_csv(bboxes: List[Dict[str, Any]], output_path: Path):
    """
    Write bounding box data to CSV file in Visual Layer format.
    
    Args:
        bboxes: List of bounding box dictionaries
        output_path: Output CSV file path
    """
    fieldnames = ['filename', 'col_x', 'row_y', 'width', 'height', 'label']
    
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(bboxes)


def main():
    """Main function to handle command line arguments and run conversion."""
    if len(sys.argv) < 2:
        input_dir = Path('boj')  # Default directory
        output_csv = Path('visual_layer_annotations.csv')  # Default output
    elif len(sys.argv) == 2:
        input_dir = Path(sys.argv[1])
        output_csv = Path('visual_layer_annotations.csv')
    else:
        input_dir = Path(sys.argv[1])
        output_csv = Path(sys.argv[2])
    
    print(f"Input directory: {input_dir}")
    print(f"Output CSV: {output_csv}")
    print("-" * 50)
    
    convert_directory_to_csv(input_dir, output_csv)


if __name__ == '__main__':
    main()