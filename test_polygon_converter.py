#!/usr/bin/env python3
"""
Unit tests for polygon to bounding box converter
Tests the core conversion logic without requiring actual files
"""

import unittest
import json
import tempfile
import os
from pathlib import Path

# Import functions from the converter (inline for testing)
def extract_polygon_points(shape):
    """Extract polygon points from a shape annotation."""
    if 'points' not in shape:
        return []
    
    points = []
    for point in shape['points']:
        if len(point) >= 2:
            x, y = int(point[0]), int(point[1])
            points.append((x, y))
    
    return points

def polygon_to_bbox(points):
    """Convert polygon points to bounding box coordinates."""
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

def process_json_data(data):
    """Process JSON data and extract bounding boxes."""
    if 'shapes' not in data:
        return []
    
    image_filename = data.get('imagePath', 'test_image.png')
    
    bboxes = []
    for shape in data['shapes']:
        if shape.get('shape_type') != 'polygon':
            continue
            
        label = shape.get('label', 'unknown')
        points = extract_polygon_points(shape)
        
        if not points:
            continue
            
        col_x, row_y, width, height = polygon_to_bbox(points)
        
        # Skip invalid bounding boxes
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


class TestPolygonToBBoxConverter(unittest.TestCase):
    """Test cases for polygon to bounding box conversion."""
    
    def test_simple_rectangle_polygon(self):
        """Test conversion of a simple rectangular polygon."""
        points = [(10, 20), (10, 30), (25, 30), (25, 20)]
        col_x, row_y, width, height = polygon_to_bbox(points)
        
        self.assertEqual(col_x, 10)  # min_x
        self.assertEqual(row_y, 20)  # min_y
        self.assertEqual(width, 15)  # max_x - min_x = 25 - 10
        self.assertEqual(height, 10) # max_y - min_y = 30 - 20
    
    def test_irregular_polygon(self):
        """Test conversion of an irregular polygon (from example data)."""
        # Points from the example QSBD annotation
        points = [(64, 42), (68, 43), (69, 41), (71, 40), (75, 40),
                  (77, 38), (77, 36), (78, 33), (76, 30), (71, 29),
                  (70, 27), (68, 26), (64, 26), (64, 29)]
        
        col_x, row_y, width, height = polygon_to_bbox(points)
        
        self.assertEqual(col_x, 64)  # min_x
        self.assertEqual(row_y, 26)  # min_y  
        self.assertEqual(width, 14)  # max_x - min_x = 78 - 64
        self.assertEqual(height, 17) # max_y - min_y = 43 - 26
    
    def test_single_point(self):
        """Test conversion of a single point (edge case)."""
        points = [(50, 60)]
        col_x, row_y, width, height = polygon_to_bbox(points)
        
        self.assertEqual(col_x, 50)
        self.assertEqual(row_y, 60)
        self.assertEqual(width, 0)   # Same point, no width
        self.assertEqual(height, 0)  # Same point, no height
    
    def test_empty_points(self):
        """Test conversion with empty points list."""
        points = []
        col_x, row_y, width, height = polygon_to_bbox(points)
        
        self.assertEqual((col_x, row_y, width, height), (0, 0, 0, 0))
    
    def test_extract_polygon_points(self):
        """Test extraction of points from shape data."""
        shape = {
            'points': [[64, 10], [64, 15], [67, 15], [68, 14], [68, 10]],
            'shape_type': 'polygon',
            'label': 'QSBD'
        }
        
        points = extract_polygon_points(shape)
        expected = [(64, 10), (64, 15), (67, 15), (68, 14), (68, 10)]
        
        self.assertEqual(points, expected)
    
    def test_extract_points_missing_key(self):
        """Test extraction when 'points' key is missing."""
        shape = {'shape_type': 'polygon', 'label': 'QSBD'}
        points = extract_polygon_points(shape)
        self.assertEqual(points, [])
    
    def test_extract_points_invalid_format(self):
        """Test extraction with invalid point format."""
        shape = {
            'points': [[64], [64, 15, 20], [67, 15]],  # Mixed valid/invalid
            'shape_type': 'polygon'
        }
        
        points = extract_polygon_points(shape)
        expected = [(64, 15), (67, 15)]  # Only valid points extracted
        
        self.assertEqual(points, expected)
    
    def test_process_complete_json(self):
        """Test processing complete JSON annotation data."""
        json_data = {
            "version": "4.5.6",
            "shapes": [
                {
                    "label": "QSBD",
                    "points": [[64, 10], [64, 15], [67, 15], [68, 14], [68, 10]],
                    "shape_type": "polygon"
                },
                {
                    "label": "QSBD", 
                    "points": [[64, 26], [68, 26], [78, 33], [64, 29]],
                    "shape_type": "polygon"
                }
            ],
            "imagePath": "test_image.png"
        }
        
        bboxes = process_json_data(json_data)
        
        self.assertEqual(len(bboxes), 2)
        
        # Check first bounding box
        bbox1 = bboxes[0]
        self.assertEqual(bbox1['filename'], 'test_image.png')
        self.assertEqual(bbox1['col_x'], 64)
        self.assertEqual(bbox1['row_y'], 10)
        self.assertEqual(bbox1['width'], 4)  # 68 - 64
        self.assertEqual(bbox1['height'], 5) # 15 - 10
        self.assertEqual(bbox1['label'], 'QSBD')
        
        # Check second bounding box
        bbox2 = bboxes[1]
        self.assertEqual(bbox2['col_x'], 64)
        self.assertEqual(bbox2['row_y'], 26)
        self.assertEqual(bbox2['width'], 14) # 78 - 64
        self.assertEqual(bbox2['height'], 7)  # 33 - 26
    
    def test_skip_non_polygon_shapes(self):
        """Test that non-polygon shapes are skipped."""
        json_data = {
            "shapes": [
                {
                    "label": "QSBD",
                    "points": [[64, 10], [64, 15], [67, 15]],
                    "shape_type": "polygon"
                },
                {
                    "label": "LINE",
                    "points": [[10, 10], [20, 20]],
                    "shape_type": "line"  # Should be skipped
                }
            ],
            "imagePath": "test_image.png"
        }
        
        bboxes = process_json_data(json_data)
        
        self.assertEqual(len(bboxes), 1)  # Only polygon should be processed
        self.assertEqual(bboxes[0]['label'], 'QSBD')
    
    def test_skip_zero_dimension_bboxes(self):
        """Test that bounding boxes with zero width or height are skipped."""
        json_data = {
            "shapes": [
                {
                    "label": "VALID",
                    "points": [[10, 10], [10, 20], [20, 20], [20, 10]],
                    "shape_type": "polygon"
                },
                {
                    "label": "ZERO_WIDTH",
                    "points": [[10, 10], [10, 20]],  # Vertical line, zero width
                    "shape_type": "polygon"
                }
            ]
        }
        
        bboxes = process_json_data(json_data)
        
        self.assertEqual(len(bboxes), 1)  # Only valid bbox should remain
        self.assertEqual(bboxes[0]['label'], 'VALID')


if __name__ == '__main__':
    print("Running polygon to bounding box converter tests...")
    unittest.main(verbosity=2)