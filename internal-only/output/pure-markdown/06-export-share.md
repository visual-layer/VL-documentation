# Export Results {#export-results}

Export detailed labeling results for quality analysis, auditing, or integration with external tools. Export is available at any stage of label propagation, even before reaching train-worthy status. Use this for quality audits or to track annotation progress across iterations.

> **Note:**  
> 
This export is optional and not required for model training through the integrated workflow.

## Export Options {#export-options}

**Visual Layer** generates a JSON file that includes detailed attribution for every labeled image, enabling you to track model accuracy and annotation quality. You can export this file as follows:

| **Export Option** | **Description** |
| :---- | :---- |
| **Export items that match the current filter selection** | Export the JSON with only the metadata for a portion of the dataset |
| **Entire Dataset** | Export the JSON for the complete dataset |
| **Label Propagation Results** | Export the JSON and all label results; this option only appears once you've completed label propagation. |
| **Include image files** | Include up to 5,000 images or only export the JSON |

**Process:**

**To export results**

1. Navigate to your dataset.

2. If relevant, filter the dataset to the results that you wish to export.

3. Click ![Download icon](images/vl-export-download-icon.png) from the top right. The **Export data** options open.

   
   
   
   ![](images/vl-export-options-dialog.png)}
   

4. Configure the export with the relevant [options](#export-options).

5. Click **Export File**.

   The JSON file downloads automatically to your default downloads folder. If you selected to export the images as well, they are downloaded in a ZIP file simultaneously.

### Example Structure for Dataset Export {#example-structure-for-dataset-export}

Use this export to work with your dataset, or portion thereof, and all of its metadata.

The structured output appears similar to the following example:

```
{
  "dataset_id": "def456",
  "timestamp": "2025-10-25T10:00:00Z",
  "total_annotations": 950,
  "total_cycles": 3,
  "annotations": [
    {
      "image_path": "images/wafer1/die_101.jpg",
      "label_name": "Surface Defect - Major",
      "source": "VL",
      "cycle_number": 3
    },
    {
      "image_path": "images/wafer1/die_102.jpg",
      "label_name": "Good Quality",
      "source": "User",
      "cycle_number": 2
    },
    {
      "image_path": "images/wafer2/die_205.jpg",
      "label_name": "Color Inconsistency",
      "source": "Seed",
      "cycle_number": 1
    },
    {
      "image_path": "images/wafer3/die_315.jpg",
      "label_name": "Structural Damage",
      "source": "VL",
      "cycle_number": 3
    }
  ]
}
```

If you export the entire dataset or a filtered portion of the dataset, the JSON file contains:

| **Field Key** | **Data Type** | **Description** |
| :---- | :---- | :---- |
| **info** | `Object` | Top-level object containing metadata about the export and dataset. |
| **schema\** | `String` | The version of the export schema. |
| **dataset** | `String` | The human-readable name of the dataset. |
| **description** | `String` | A brief description of the export operation. |
| **dataset\** | `String` | A URL pointing to the dataset within the **Visual Layer** application. |
| **export\** | `String (ISO 8601)` | Timestamp indicating when the data export was initiated. |
| **dataset\\** | `String (ISO 8601)` | Timestamp indicating when the dataset was originally created. |
| **exported\** | `String` | The user who performed the data export. |
| **total\\** | `Integer` | The total number of images/media items in the dataset. |
| **media\** | `Array of Objects` | Array containing details for each image in the export (similar to the results array in the standard example, but with richer media details). |
| **media\** | `String` | Unique identifier for the media item (image). |
| **media\** | `String` | The type of media (e.g., "image"). |
| **file\** | `String` | The original file name of the image. |
| **file\** | `String` | The path to the file within the original AOI output structure. |
| **file\** | `String` | The size of the image file. |
| **uniqueness\** | `Number (Float)` | A score indicating how unique the image is compared to the rest of the dataset. |
| **height** | `Integer` | The height of the image in pixels. |
| **width** | `Integer` | The width of the image in pixels. |
| **url** | `String` | A URL to view the specific media item in **Visual Layer**. |
| **cluster\** | `String` | The ID of the visual cluster the image belongs to (from the Exploration features). |
| **metadata\** | `Array of Objects` | Array containing application-specific or custom metadata related to the image. |
| **type** | `String` | The type of metadata entry (e.g., "issue", "image\"). |
| **properties** | `Object` | Object containing specific details for the metadata item type. |
| **issue\** | `String` | Specific classification of the issue (e.g., "mislabels"). |
| **issues\** | `String` | A description or source of the issue. |
| **confidence** | `Number (Float)` | A confidence score associated with the metadata/issue. |

### Example Structure for Label Propagation Export {#example-structure-for-label-propagation-export}

Use this export to track the source of each label to measure model accuracy and identify areas for improvement:

| **Use Case** | **Description** |
| :---- | :---- |
| **Model acceptance rate** | How often VL automatic labels were approved versus corrected |
| **Class-specific performance** | Which defect types the model handles well versus those needing more training data |
| **Quality assurance** | Full audit trail for compliance and process validation |
| **Training integration** | Traceable labeled data for your model pipeline |

The structured output appears similar to the following example:

```
{
  "dataset_id": "abc123",
  "results": [
    {
      "image_id": "img_001",
      "label": "Surface Defect - Minor",
      "source": "VL",
      "confidence": 0.94
    },
    {
      "image_id": "img_002",
      "label": "Good Quality",
      "source": "User",
      "confidence": null
    },
    {
      "image_id": "img_003",
      "label": "Structural Damage",
      "source": "Seed",
      "confidence": null
    }
  ]
}
```

The JSON file contains the following information:

| **Field** | **Data Type** | **Description** |
| :---- | :---- | :---- |
| **dataset\** | `String` | A unique identifier for the dataset. |
| **timestamp** | `String (ISO 8601)` | The date and time when the label propagation results were exported. |
| **total\** | `Integer` | The total number of images that received a label (either automatic or manual) in this dataset. |
| **total\** | `Integer` | The total number of label propagation iterations/cycles completed on this dataset. |
| **annotations** | `Array of Objects` | A list containing the labeling result details for each image. |
| **image\** | `String` | The file path of the image within the original directory structure of the dataset. |
| **label\** | `String` | The final class/label assigned to the image. |
| **source** | `String` | The origin of the assigned label: user (manual assignment/review), seed (initial user-provided example), or VL (**Visual Layer** automated assignment). |
| **cycle\** | `Integer` | The label propagation iteration number when the label was assigned or last reviewed. |