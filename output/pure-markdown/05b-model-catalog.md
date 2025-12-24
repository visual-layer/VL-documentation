# Train Models: Model Catalog {#the-model-catalog}

The **Model Catalog** is the central hub for managing your downstream model training and results. Once an external model training job successfully completes, the trained model data is accessible from the **Model Catalog**. From here, you can:

* View detailed training results in HTML format
* Export the entire model results folder as a ZIP file
* Delete models from the **Visual Layer** catalog

**Process:**

To get started

From the left of the **Visual Layer** interface, click ![](images/vl-modelcatalog-icon.png).

The **Model Catalog** loads, and appears similar to the following:

![Model Catalog](images/vl-training-model-catalog.png)

## Catalog Structure and Features

The **Model Catalog** displays a table view of all the models you've sent data to for training. All columns support filtering and ascending/descending sorting for easy navigation.

The table displays the following information:

| **Column** | **Description** |
| :---- | :---- |
| **Model Name** | The name of the selected model, as returned from Camtek. |
| **Type** | The type of the model. This is currently always **Classification**. |
| **Source** | The training source. This is currently always Camtek Auto ML. |
| **Dataset Name** | The human-readable name of the dataset in **Visual Layer** used for training. |
| **Dataset ID** | The unique system identifier of the training dataset in **Visual Layer**. |
| **Job** | The production job identifier for the training job. |
| **Setup** | The machine setup configuration used. |
| **Recipe List** | A list of the scanning recipes applied. |
| **Tool List** | The tools used. |
| **Last Updated** | The timestamp from the training job results folder. |
| **Results** | Click the icon to view the HTML report. The report is embedded within **Visual Layer** for easy access. |
| **Production** | Check or uncheck to mark models as production-ready. Unchecking requires confirmation: "Confirm removal from production - You are about to unmark this model as production. Are you sure?" |
| **Three-Dot Menu** | Provides key functions for managing trained models: **Export** downloads the entire model results folder as a ZIP file to your local Downloads folder. **Delete** removes the model entry from the catalog (requires confirmation, elevated users only). |

**Process:**

To remove a model from production

1. Uncheck the **Production** checkbox for the relevant model.

   A confirmation modal appears:

   
   
   ![](images/vl-modelcatalog-production-remove-confirmation.png)
   
**Remove from Production Confirmation**

   

2. Click **Yes** to confirm the removal (or **Cancel** to keep the production status).

   The model is unmarked as production.

**Process:**

To delete a model from the catalog

1. From the relevant row in the **Model Catalog**, click the three-dot menu and choose **Delete**.

   A confirmation modal appears:

   
   
   ![](images/vl-modelcatalog-deletemodel-confirmation.png)
   
**Delete Model Confirmation**

   

2. Click **Yes, delete** to confirm (or **Cancel** to stop).

   The model entry is immediately removed from the catalog interface.

> **Important:**  
> 
Deleting a model from the catalog does not delete the model files from disk. The files remain in their original location.

## Understanding Model Training Results

When model training completes successfully, Camtek generates comprehensive validation reports that assess your trained model's classification performance. These reports help you evaluate model accuracy, identify areas for improvement, and make informed decisions about deploying models to production.

The training results package includes two main HTML reports along with supporting data files:

* **Validation Summary** - Overview of model performance with confusion matrix and per-class metrics
* **Sample Metrics Report** - Detailed per-image uncertainty and confidence metrics
* Supporting CSV files with predictions, logits, and confusion matrix data
* Transformed debug images showing model processing

**Process:**

To access training results

1. To view the **Validation Summary** report from your browser, click ![](images/vl-modelcatalog-view-results.png) in the **Results** column. 

   OR

   To export results, click the three-dot menu for the relevant model and choose **Export**.

   The entire results folder downloads as a ZIP file to your Downloads folder.

3. Extract the ZIP file.

   The extracted folder contains:

   * `summary/validation_summary.html` - Main validation report
   * `sample_metrics_report/report.html` - Detailed metrics report
   * `summary/predictions.csv` - Image-by-image predictions
   * `summary/confusion_matrix.csv` - Classification confusion matrix
   * `summary/logits.csv` - Raw model output scores
   * `summary/missed_images_data.js` - Misclassified samples data
   * `summary/images_debug_transformed/` - Processed image directory
   * `sample_metrics_report/images/` - Original images directory
   * `js/` and `style/` - Required JavaScript and CSS files

4. Double-click the `html` file for the relevant report to open it in your browser.

> **Tip:**  
> 
Save the extracted results folder for your records. The reports remain fully functional offline.

### Validation Summary Report

The **Validation Summary** report provides a comprehensive overview of your trained model's performance on the validation dataset.

#### General Information

The report header displays key metadata about the training run:

![Training Run Metadata](images/vl-modelcatalog-results-general.png)

Fields include: 

| **Field** | **Description** |
| :---- | :---- |
| **Tag** | Identifier for this training run and model configuration |
| **Generated on** | Date and time when the validation report was created (YYYY-MM-DD HH:MM:SS format) |
| **Data path** | Location of the validation dataset used to evaluate model performance |
| **Checkpoint** | Path(s) to the trained model checkpoint file(s) |
| **Dataset size** | Total number of images in the validation set and the split used |
| **FPR@95%TPR (OOD)** | False Positive Rate at 95% True Positive Rate for out-of-distribution detection |

#### Class Distributions by Zone

An expandable histogram section showing how samples are distributed across different inspection zones and classes. 

![Class Distribution by Zone](images/vl-modelcatalog-results-classbyzone.png)

This helps identify data imbalances that may affect model performance.

#### Confusion Matrix

The confusion matrix displays actual ground truth classes versus predicted classes, with color coding to highlight classification performance:

![Confusion Matrix](images/vl-training-confusion-matrix-example.png)

Rows represent actual ground truth labels, while columns show predicted labels. The matrix includes performance metrics:

| **Metric** | **Description** |
| :---- | :---- |
| **FP Rate** | False Positive Rate - percentage of negative samples incorrectly classified as this class |
| **Precision** | Percentage of predictions for this class that were correct |
| **Recall** | Percentage of actual instances of this class that were correctly identified |
| **Accuracy** | Overall percentage of correct classifications for this class |
| **F1-Score** | Balanced measure combining Precision and Recall |

The diagonal cells (where actual equals predicted) represent correct classifications and are highlighted with darker green shading. Off-diagonal cells show misclassifications with lighter shading or red tones.

#### Defects Data Table

The detailed defects table displays every image in the validation set with its actual and predicted classifications. 

![Confusion Matrix](images/vl-training-defectsdata-example.png)

**Process:**

Use the dropdown filters to

* **Actual** - Filter by ground truth class
* **Predicted** - Filter by model prediction

This table helps you identify specific misclassification patterns and review individual model decisions.

### Sample Metrics Report

The **Sample Metrics** report provides detailed uncertainty and confidence metrics for each image in the validation set. 

![Sample Metrics report](images/vl-training-sample-metrics-example.png)

This advanced report helps you:

* Identify images where the model is uncertain
* Understand prediction confidence levels
* Compare performance between different model architectures (SWINV2 vs CLIP)
* Detect potential data quality issues

The report includes per-image metrics:

| **Metric** | **Description** |
| :---- | :---- |
| **Margin** | Difference between top prediction and second-best prediction (higher = more confident) |
| **Entropy** | Measure of prediction uncertainty (lower = more confident) |
| **Energy** | Alternative confidence measure based on logits |
| **Predicted Ratio** | Ratio of top prediction probability |
| **Ensemble Disagreement** | Disagreement between multiple model architectures |

Metrics are provided for:

* **Combined** - Ensemble metrics across all models
* **SWINV2** - Vision transformer model metrics
* **CLIP** - Multimodal model metrics

Each metric includes both average and standard deviation values to capture prediction stability.