# Evaluate Label Propagation {#evaluating-label-propagation}

After completing label propagation, you can validate the accuracy of the automatically generated labels. The **LP Auto Annotation Validation Report** is an interactive HTML report comparing your Ground Truth data with the labels generated through the label propagation process. 

Use the evaluation report to make informed decisions about your label propagation quality:

  - Measure overall accuracy to determine if your dataset is ready for model training
  - Identify which defect classes need additional seed examples or clearer definitions based on per-class precision
  - Track error sources by label origin to determine whether additional review iterations or annotation guideline clarification is needed
  - Locate classes with high missed detection rates requiring more diverse seed examples
  - Export validation data for compliance documentation and process audits

## Prerequisites

Before generating an evaluation report, ensure you have:

* Completed the [label propagation](#how-label-propagation-works) feedback loop for the dataset
* A Ground Truth file (`db.csv`) containing validated annotations for your images
* A class mapping file (`classes.json`) defining the taxonomy used in your Ground Truth data

> **Note:**  
> 
The Ground Truth taxonomy must align with the classes used during label propagation. Additionally, in this file, the Image Name column which includes the relative path must include the folder name in which the image is saved.

## Generate an Evaluation Report 

The report includes:

* High-level accuracy metrics and summary statistics 
* A breakdown of the user input accuracy
* Confusion matrix showing classification performance across all classes
* Image-by-image comparison of Ground Truth versus Label Propagation results
* Visual examples highlighting agreement and discrepancies

> **Note:**  
> 
See [Report Structure and Details](#report-structure-and-details) for more information. 

An example evaluation report appears similar to the following:

![](images/vl-camtek-evaluation-report-example.png)

**Evaluation Report Example**

**Process:**

**To create an evaluation report**

1. Navigate to your dataset in **Visual Layer**.

   Ensure label propagation is complete for the dataset you want to evaluate.

2. Go to the three-dot menu and click ![](images/vl-evaluation-icon.png) **Evaluate Label Propagation**.

   
> **Note:**  
> 
   The **Evaluate Label Propagation** option appears only after label propagation has finished running.
   

   The **Evaluate Label Propagation** dialog appears.

   ![](images/vl-labelpropagation-evaluation.png)

3. Click **Browse Folders** and provide the paths to your Ground Truth files:

   * `db.csv` - Your validated image classifications
   * `classes.json` - The defect taxonomy definition

   
> **Important:**  
> 
   The Ground Truth files must use the same class names and structure as your Label Propagation configuration. Mismatched taxonomies will prevent report generation.
   

4. Click **Run Evaluation**.

   A progress notification appears showing the comparison status. The system validates your files, matches image names, compares classifications, and generates the HTML report.

5. When processing completes, a notification confirms the report is ready.

   The report downloads automatically as a ZIP file to your Downloads folder. The ZIP contains:

   * `index.html` - located in the root of the folder , this is the report itself (viewable in Chrome)
   * `js/` - Required JavaScript files (Chart.js and report functionality)
   * `style/` - CSS styling files
   * `DB.csv` - Merged comparison data (including class IDs)
   * `classes.json` - Class mapping reference (maps IDs to class names)
   * `missed_images_data.js` - Data file for mismatched samples

6. Extract the ZIP file.

7. Double click the `index.html` file in the root of the folder to open the report in your Chrome browser.

> **Tip:**  
> 
Save the extracted report folder for your records. The report remains fully functional offline.

**Process:**

**To explore and analyze the report data**

* In any table, hover over a cell or row to highlight its position more clearly. 
* Slice and dice the [**Image Classification Validation**](#image-classification-validation) table via various filters. 

## Report Structure and Details

The evaluation report contains the details and insights as described in this section.

### General Information

The report header provides an at-a-glance understanding of how well your label propagation performed across the entire dataset. This summary displays key metrics and metadata about your validation:

![General Informaion Example](images/vl-camtek-evaluationreport-sections1-2-examples.png)

| **Field** | **Description** |
| :---- | :---- |
| **Generated On** | Date and time when the report was created (YYYY-MM-DD HH:MM:SS format) |
| **Total Samples** | The total number of sample images that were given for the seed from this dataset |
| **Number of Classes** | Total number of classes (labeled) included in the label propagation |
| **Class breakdown** | A list of the classes, their class IDs, and the total number of images in each class. For example, 1 - butterfly (92) means the class ID is 1, the class name is butterfly, and 92 images were labeled with this class. |

### LP Auto Annotation Performance

This section evaluates how closely the Label Propagation results match the Ground Truth, appearing similar to the following example: 

![LP Auto Annotation Performance Example](images/vl-camtek-evaluationreport-lpautoannotationperformance-examples.png)

#### Per-Class Performance

This table displays detailed classification performance metrics for each class.

| **Metric** | **Description** | **Formula** |
| --- | --- | --- |
| **Class** | The name of the class for these statistics |
| **Precision** | Percentage of Label Propagation predictions that were correct for this class | True Positives / (True Positives + False Positives) |
| **Recall** | Percentage of actual instances that Label Propagation correctly identified | True Positives / (True Positives + False Negatives) |
| **F1-Score** | Balanced measure combining Precision and Recall | 2 × (Precision × Recall) / (Precision + Recall) |

#### Confusion Matrix

The confusion matrix table displays the predicted classes versus the ground truth. Rows represent the actual Ground Truth labels, while columns show the predicted Label Propagation results.

Each cell in the matrix displays the count of images where a Ground Truth class (row) was predicted as a specific Label Propagation class (column). The diagonal cells (where row equals column) represent correct classifications.

The matrix includes:

* **Row Totals (GT Total)** - The total number of images for each Ground Truth class
* **Column Totals (Predicted Total)** - The total number of images predicted for each class by Label Propagation

![Confusion Matrix Example](images/vl-camtek-evaluation-confusionmatrix-example.png)

> **Note:**  
> 
For datasets with many classes, the matrix displays class IDs with a mapping reference at the top of the table. Use horizontal scrolling to view all columns.

### User Performance Overview

This section of the report provides an overview of the user's performance during Label Propagation as compared to the ground truth, which is divided into sub-sections: 

![User Performance Overview Example](images/vl-camtek-evaluation-userperformance-example.png)

#### Summary

The summary itemizes: 

* Total Questions Answered - the total number of feedback requests that the user responded to 
* Total User Errors - the number of errors that the user made in total
* Seed-Stage Errors - the number of initial seed samples that the user provided incorrectly 
* Review-Stage Errors - the total number of feedback requests that the user responded to incorrectly

#### User Errors per Class

This table displays the details of user errors **per class** for:

* seed stage
* review stage 
* in total 

### Image Classification Validation

The final section displays every image in your dataset with its Ground Truth and Label Propagation classifications side by side. This detailed view enables you to:

* Review individual classification decisions
* Filter images by Ground Truth class, Label Propagation class, match status, or label source
* Identify patterns in misclassifications
* Audit specific defect types requiring attention

![Image Classification Validation Example](images/vl-camtek-evaluation-imageclassification-example.png)

**Process:**

To manipulate data in this table:

 

1. Sort by any column. Click the title of the column to change sorting direction. 

2. Filter with these options: 

      * GT Classification - view images by a specific ground truth classification 
      * LP Classification - view images by a specific label propagation classification 
      * Result - filter by whether the label propagation was correct or incorrect
      * Source - filter by the source of the label application - Visual Layer (the model), seed or the user (during review stages)

3. View the continuation of the table from the page arrows at the top right of the table. 

4. Click **Clear Filters** to view the entire table. 