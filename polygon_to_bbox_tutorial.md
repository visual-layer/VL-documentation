# Converting Polygon Annotations to Visual Layer Bounding Box Format

This tutorial demonstrates how to convert polygon annotations from JSON files to Visual Layer's bounding box CSV format.

## Overview

The example data in the `boj/` directory contains:
- An image file: `procuct(1)-0_SEQUENCE_A-rawImge_tag_0_crop_3_time_2023_10_9_17_39_21.png`
- A JSON annotation file with the same name containing polygon annotations

The JSON file contains polygon annotations with:
- Multiple shapes with polygon coordinates
- Labels (e.g., "QSBD")
- Each polygon defined by an array of [x, y] points

## Target Format

Visual Layer bounding box format requires CSV with columns:
- `filename`: Image filename
- `col_x`: Left x-coordinate of bounding box
- `row_y`: Top y-coordinate of bounding box  
- `width`: Width of bounding box
- `height`: Height of bounding box
- `label`: Object class label

## Conversion Process

1. **Extract polygon coordinates**: Read JSON files and extract point arrays
2. **Calculate bounding box**: Find min/max x,y coordinates to create bounding rectangle
3. **Format output**: Generate CSV in Visual Layer format

## Example Data Structure

The JSON annotations contain shapes like:
```json
{
  "label": "QSBD",
  "points": [
    [64, 10], [64, 15], [67, 15], [68, 14], [68, 10]
  ],
  "shape_type": "polygon"
}
```

This gets converted to a bounding box by:
- `col_x` = min(x_coordinates) = 64
- `row_y` = min(y_coordinates) = 10  
- `width` = max(x_coordinates) - min(x_coordinates) = 68 - 64 = 4
- `height` = max(y_coordinates) - min(y_coordinates) = 15 - 10 = 5

## Python Implementation

See the accompanying Python script for the complete implementation.