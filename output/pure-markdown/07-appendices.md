

# User Interface Reference

This reference guide provides detailed descriptions of all **Visual Layer** screens, components, and interface elements. Use this section to understand what each field, button, and area of the platform does.

## Home Page: Dataset Inventory {#dataset-inventory}

When you log in to **Visual Layer**, the home page displays the **Dataset Inventory**:

![**Visual Layer** Platform](images/vl-landing-overview.png)

The home page layout consists of:

| **Area** | **Name** | **Description** |
| --- | --- | --- |
| ![](images/1light.png) | **Navigation Panel** | Navigate to: this area (the **Dataset Inventory**, which is your **Home** page), the **Task Manager**, the **Model Catalog**, and log in/log out |
| ![](images/2light.png) | **Main Panel** | Search for datasets. |
| ![](images/3light.png) | **Dataset Inventory** | This is your default Home page, as appears in the example above. The **Dataset Inventory** page displays a complete list of your datasets. Click any dataset to open it. |
| ![](images/4light.png) | 1m{0.35|}![](images/vl-create-dataset-create-button.png)% | Create a new dataset. |

### Navigation Panel {#nav-panel}

The **Navigation Panel** provides access to all major areas of **Visual Layer**:

| **Icon** | **Name** | **Description** |
| --- | --- | --- |
| ![](images/vl-dataset-inventory-icon.png) | **Dataset Inventory** | A complete list of your datasets. |
| ![](images/vl-task-manager-icon.png) | **Task Manager** | Monitor and manage all active tasks, jobs, and processing workflows. |
| ![](images/vl-modelcatalog-icon.png) | **Model Catalog** | Browse, deploy, and manage trained models for inference and analysis. |
| ![](images/vl-avatar-icon.png) | **Your Avatar** | Log out of your account. |

### Dataset Inventory View

The **Dataset Inventory** displays all datasets as cards:

![](images/vl-dataset-inventory-view.png)

![](images/vl-dataset-inventory-cards.png)

#### Dataset Card

Each dataset card shows:

![](images/vl-dataset-inventory-card.png)

**Dataset Card Example**

| **Field** | **Description** |
| :---- | :---- |
| **Dataset Name** | The title of the dataset for easy identification and reference. |
| **Creation Date** | The date when the dataset was created and added to your inventory. |
| **Dataset Status** | Current state of the dataset: **Ready**, **Processing**, **Failed**, or **Archived**. |
| **Image Count** | Total number of images contained in the dataset. |
| **Info Icon** ![](images/vl-info-i-icon.png) | Hover to view associated Job Name, Setup Name, and Recipe Names. |
| **Three-Dot Menu** | Access dataset actions including **Delete**. |

![](images/vl-camtek-datasetinventory-metadata.png)

**Dataset Metadata Popup Example**

### Main Panel Controls

The **Main Panel** provides dataset management tools:

![](images/vl-main-nav-panel.png)

| **Control** | **Description** |
| :---- | :---- |
| **Search Bar** | Locate datasets by name. |
| **Filter by Job/Recipe/Setup** | Filter datasets by production metadata (Job Name, Setup Name, Recipe Name). |
| **Sort By** | Arrange datasets based on status, creation date, or other attributes. |
| **Clear Selection** | Reset applied filters. |

## Dataset View

When you open a dataset, the main dataset exploration interface loads:

![Dataset View with Details](images/vl-overview-cluster-view.png)

The dataset view consists of:

| **Area** | **Component** | **Description** |
| --- | --- | --- |
| ![](images/1light.png) | **Tabs** | Navigate between Explore, Data and Views. |
| ![](images/2light.png) | **Filter Panel** | Apply and combine search criteria. |
| ![](images/3light.png) | **Action Bar** | Access operations like exporting. |
| ![](images/4light.png) | **Details Sidebar** | View metadata and insights, and access label propagation. |
| ![](images/5light.png) | **Thumbnail Grid** | Visual representation of your data in clusters. |

### Dataset Metadata

Hover over the info icon ![](images/vl-info-i-icon.png) next to the dataset name to view production metadata:

![](images/vl-camtek-dataset-metadata.png)

**Dataset Metadata Popup**

| **Field** | **Description** |
| :---- | :---- |
| **Job Name** | The production job identifier from the folder metadata. |
| **Setup Name** | The setup configuration identifier from the folder metadata. |
| **Recipe Names** | The recipe name(s) used during inspection. |

### Cluster View {#clustering-granularity}

**Visual Layer** automatically groups similar images into clusters during dataset creation. Each cluster is displayed as a preview card:

![Cluster preview cards](images/vl-clusters-image-view.png)

| **Cluster Card Element** | **Description** |
| :---- | :---- |
| **Number of items** | The total number of items that match your current filters |
| **Prominent labels** | The most frequent labels within the cluster |
| **Representing images** | Thumbnails of a few key example images that visually summarize the cluster |
| **Visual Similarity Icon** ![](images/vl-visual-similarity-icon.png) | Hover over a cluster to access visual similarity search |

### Filter Menu

Access filters by clicking ![](images/vl-filterbutton.png) in the dataset toolbar:

![All Filters](images/vl-camtek-allfilters.png)

#### Available Filters

| **Filter Category** | **Description** | **Configuration** |
| :---- | :---- | :---- |
| **Folders** | Filter by specific AOI output folders within your dataset | Check the folders to include |
| **Files** | Filter by specific image files or file patterns | Enter filename or pattern to match |
| **Labels** | Filter by assigned label classes | Select which classes to include or exclude |
| **User Tags** | Filter by custom tags you've applied to images | Select tags from your tag list |
| **Duplicates** | Show only duplicate or near-duplicate images | Toggle on to show duplicates only |
| **Outliers** | Show images that differ significantly from typical patterns | Toggle on to show outliers only |
| **Quality Issues** | Filter images flagged with quality problems | Select issue types (blur, overexposure, underexposure, etc.) |
| **Select Uniques** | Show only unique images (exclude duplicates) | Toggle on to show unique images only |
| **Insertion Time** | Filter by when images were added to the dataset | Set date ranges for upload time |
| **Media Status** | Filter by processing or indexing status | Select status types (pending, processing, ready, error) |

#### Applied Filters Display

Applied filters appear in the **Query Panel** above the image grid:

![Applied Filters](images/vl-applied-filters.png)

| **Control** | **Description** |
| :---- | :---- |
| **Filter Chip** | Each applied filter shows as a chip with its criteria |
| **X Button** | Click to remove an individual filter |
| **Clear All** | Remove all applied filters at once |

> **Note:**  
> 
Multiple filters combine using **AND** logic.

### Visual Similarity Search {#visual-search}

**Visual Layer** enables similarity search using deep visual embeddings:

| **Search Method** | **Action** |
| :---- | :---- |
| **From cluster or image in cluster view** | Hover over a cluster or the image and click ![](images/vl-visual-similarity-icon.png) at the bottom of the card. |
| **From the Image Details Page** | Click a single image to open its details page, then click ![](images/vl-visual-similarity-BUTTON.png) from the **Action Bar**. |
| **Using an External Image** | Click ![](images/vl-visual-similarity-searchbaricon.png) near the search bar inside your dataset, upload an image from your device, optionally crop it, and start the search. |

### Views Tab

The **Views** tab displays saved filter combinations and search queries:

| **Control** | **Description** |
| :---- | :---- |
| **Save as View** Button | ![Save as View button](images/vl-save-view-button.png) <br/>Saves current filters and search criteria as a reusable view |
| **View Name** Dialog | ![Name the View dialog](images/vl-save-view-dialog.png) <br/>Enter a descriptive, unique name for the view |
| **View Card** | Click any saved view to load its filter combination |
| **Three-Dot Menu** | Access view actions including **Delete** |
| **Delete Confirmation** | ![Confirm Deletion](images/vl-dataset-views-delete-confirmation.png) |
| **Delete Notification** | ![Delete Notification](images/vl-dataset-views-delete-notification.png) |

> **Note:**  
> 
Views are immutable. To modify a view, delete it and create a new one with updated criteria.

# Dataset Creation Stages {#dataset-creation-stages}

During dataset creation, **Visual Layer** prepares the dataset for exploration through the following stages:

| **Status** | **Description** |
| :---- | :---- |
| **NEW** | Dataset initialization started |
| **UPLOADING** | Upload request acknowledged, data transfer in progress |
| **INITIALIZING** | Pre-processing setup in progress |
| **PRE_PROCESSING** | Data prepared for indexing and analysis |
| **INDEXING** | Visual indexing and AI-based analysis in progress: learning distribution patterns and creating enhanced embeddings tailored to your data for label propagation accuracy |
| **SAVING** | Final data save to system in progress |
| **READY** | Dataset complete and available for exploration |
| **FATAL_ERROR** | Irrecoverable failure during dataset creation; check error details in notification or **Task Manager** |

# Dataset Operation Statuses {#dataset-operation-statuses}

After dataset creation (or dataset update), dataset status appears on its card in the **Dataset Inventory** and inside the dataset at the top right. Statuses indicate the current state and availability of dataset operations:

| **Status** | **Description** |
| :---- | :---- |
| **READY** | No blocking operations are running. All actions are available. |
| **UPDATING** | A blocking operation is running (**Label Propagation** or **Re-indexing**). Most dataset actions are unavailable until the operation completes. |
| **CREATING** | The dataset is being created. No dataset actions are available until creation completes. |
| **RESUME** | User action is required to complete dataset creation. Data upload started but **Create Dataset** was not clicked. |
| **PENDING** | New media was added and requires re-indexing. |

> **Note:**  
> 
A dataset can show **Ready** status in the **Dataset Inventory** even when the **Task Manager** displays completed tasks like **Training** <!-- or **Media Addition**,  -->since these operations do not block dataset access.

# Task Manager Statuses {#task-manager-statuses}

Tasks are operations you perform in the system, such as creating a dataset, updating an existing dataset or running label propagation. All tasks in the **Task Manager** display one of the following statuses to indicate their current state. Each status includes a percentage to show progress through the operation:

| **Status** | **Description** |
| :---- | :---- |
| **Initializing** | The operation is performing initial validations, uploading data, or downloading resources. Progress percentage reflects completion of initialization steps. |
| **Running** | The operation is actively processing. Progress percentage reflects completion of the overall operation. |
| **Succeeded** | The operation completed successfully. Progress shows 100%. |
| **Failed** | The operation encountered an error and could not complete. Hover over the status to view the error message explaining what went wrong. |
| **Aborted** | The operation was manually stopped by a user before completion. |
| **Waiting for Review** | The label propagation operation completed and is ready for your review. Navigate to the dataset to begin reviewing propagated labels. This status applies only to **Label Propagation** tasks. |

# Model Training Statuses {#training-status-reference}

When you initiate model training, **Visual Layer** displays real-time progress updates showing the current status and completion percentage (0-100%). The training process progresses through the following stages:

| **Status** | **Description** |
| :---- | :---- |
| **Waiting for Start** | Training job is queued and waiting to begin. |
| **Running** | Model training is actively in progress. Progress updates in real-time. |
| **Completed Successfully** | Training finished successfully. Model is ready in the Model Catalog. |
| **Exited** | Training process exited before completion. |
| **Failed** | Training encountered an error. Hover over the status to view error details. |

# Progress Indicators {#progress-indicators-reference}

**Visual Layer** provides multiple progress indicators throughout the label propagation workflow to help you track completion status and make informed decisions about when to finish. These indicators appear during both seed creation and iterative review phases.

## Seed Creation Progress

During seed creation, visual indicators show when you've met the minimum requirement of 5 examples per class. Each class displays a progress indicator that fills as you add examples:

![](images/vl-labelpropagation-progress-indicator.png)

**Seed Selection Progress Indicator**

When all classes show complete indicators (5+ examples each), the **Submit** button becomes enabled, allowing you to begin label propagation.

## Label Propagation Progress

**Visual Layer** requires 100 labeled images per class as the minimum threshold for training readiness. The platform provides three distinct progress indicators to track your advancement:

### Train-worthy Progress

Shows progress toward the 100 images per class training readiness goal. When this reaches 100%, you have met the minimum threshold required to train models downstream.

![](images/vl-review-trainworthy-progress.png)

**Train-worthy Progress**

This indicator focuses on whether you've reached the training threshold, not on labeling your entire dataset.

### Overall Progress

Shows the percentage of your entire dataset that has been labeled, regardless of the per-class training threshold. This indicates how much of your total dataset has received labels.

![](images/vl-review-overall-progress.png)

**Overall Progress**

Use this indicator to understand dataset completion as a whole, independent of training requirements.

### Per-Class Progress

Shows how many labeled images each individual class has toward the 100-image minimum threshold. Use this to identify which classes need more labeled examples before you can train models.

![](images/vl-review-perclass-progress.png)

**Per-Class Progress**

This granular view helps you prioritize review efforts for classes that haven't reached the training threshold yet.

# Troubleshooting Common Issues

This section provides solutions to errors and problems you might encounter while working with **Visual Layer**. Each issue includes an explanation of what went wrong and specific steps to resolve it.

## Dataset Creation and Media Upload Errors

When uploading folders or adding media to datasets, **Visual Layer** validates that all required files exist and are structured as expected. If validation fails, you'll see one of these error messages:

| **Error** | **What It Means** | **How to Fix** |
| :---- | :---- | :---- |
| **Missing required files** | Your folder is missing one or more required files: db.csv, metadata.json, classes.json, or db_export_\*.json | Check that the AOI scan completed successfully. All four file types must be present in the folder. |
| **Invalid file naming** | The db_export file doesn't follow the expected naming pattern | Rename the file to match the pattern: db_export_\[id\].json (for example, db_export_12345.json) |
| **JSON parsing error** | The classes.json or db_export file contains syntax errors | Open the file in a JSON validator to identify and fix formatting issues (missing commas, quotes, brackets, etc.) |
| **Cross-validation failure** | Job Name, Setup Name, or Recipe Name don't match between files within the same folder | The metadata.json file may be corrupted. Try regenerating the scan from the AOI machine. |
| **Job Recipe mismatch** | Job Name, Setup Name, Recipe Name, or Tool List differs between folders you're trying to combine—or doesn't match the original dataset when adding media | For new datasets: Only combine folders from the same production run. For adding media: Ensure the new folder came from the exact same Job/Setup/Recipe as the original dataset. |
| **ImageName mismatch** | Filenames listed in db.csv don't match the actual image files in the folder | Check that the ImageName column in db.csv contains exact filenames with extensions. Fix any typos or missing extensions. |
| **Class taxonomy mismatch** | The classes.json file defines different classes than the original dataset | When adding media to an existing dataset, you must use the identical classes.json file from the original dataset creation. Classes cannot be changed when adding media. |

## Label Propagation

These issues might arise during seed creation and iterative review. Most problems stem from insufficient or unrepresentative seed examples.

| **Problem** | **Description** | **Resolution** |
| :---- | :---- | :---- |
| Inaccurate results for certain defect types | The model consistently mislabels specific defect types. High-confidence automatic labels are frequently incorrect during review. | Add more diverse seed examples showing the full range of that defect type's visual variations. Avoid using edge cases or ambiguous examples as initial seeds. Reset if needed to start with improved seeds. |
| Cannot drag multiple selected items to assign labels | You're trying to drag multiple selected images to a class label, but only single items can be dragged. | Use the Select & Add workflow instead: select multiple images using checkboxes, click **Assign Label**, then choose the target class from the dropdown. |

# Frequently Asked Questions

**Q: Why do review batches keep appearing? How many times do I need to review?**

A: Label propagation is an iterative process where each review round improves the model's accuracy. Continue reviewing until Visual Layer reaches high confidence across your dataset or you're satisfied with the labeling progress. The number of iterations varies based on dataset complexity and seed quality.

**Q: Why can't I edit my seed examples after starting label propagation?**

A: Seeds become immutable once propagation begins to ensure consistency throughout the iterative learning process. If you need to change seeds or classes, use Reset to start over. Note that this permanently deletes all label propagation progress but preserves your original dataset.

**Q: What do the source indicators (VL, User badges) mean?**

A: These badges show the origin of each label. **VL** means the label was assigned by Visual Layer with high confidence. **User** means you reviewed and confirmed the label in a previous iteration. Seed examples appear without a badge. See [Reviewing and Providing Feedback](#reviewing-and-providing-feedback) for complete definitions.

**Q: Can I run label propagation on the same dataset multiple times?**

A: Yes. However, each new run will overwrite the previous results within that dataset.

**Q: What happens to images I marked as "Ignore"?**

A: They are excluded from label propagation, placed in an "Unlabeled" cluster, and don't count toward training readiness or review quotas.

**Q: Can I export data before reaching "Train Worthy" status?**

A: Yes. You can export label propagation results at any point using Export, even if you haven't reached the 100 images per class threshold.

**Q: How do I know if my seed examples are good quality?**

A: Monitor first-iteration results. If many high-confidence automatic labels are incorrect during your first review, your seed likely needs improvement. Reset and select clearer, more representative examples.

**Q: Can I combine datasets from different Jobs/Setups/Recipes?**

A: No. Each dataset must contain folders with identical Job, Setup, and Recipe metadata. Create separate datasets for different production runs, then filter and organize them using the metadata filters.

**Q: Why are some folders grayed out when I try to add media or create a dataset?**

A: Visual Layer automatically validates metadata compatibility. Grayed-out folders indicate their Job, Setup, Recipe, or Tool List metadata doesn't match the other selected folders. Hover over the info icon to view the specific mismatch. You can either select only folders with matching metadata, or create separate datasets for incompatible production runs.

**Q: How do I fix incorrect seed examples or classes after starting label propagation?**

A: Use Reset to start over with new seeds or classes. This permanently deletes all label propagation progress but preserves your original dataset. Seeds become immutable once propagation begins to ensure consistency throughout the iterative learning process, so resetting is the only way to change them.

**Q: Why haven't I reached train-worthy status after multiple review rounds?**

A: Visual Layer requires a minimum of 100 images per class for training readiness. Continue review rounds until this threshold is met. If progress is very slow, verify you have sufficient unlabeled data in your dataset and consider adding more images. The number of iterations needed varies based on dataset size, complexity, and seed quality.

# Terms and Definitions

| **Term** | **Definition** | **Example/Context** |
| :---- | :---- | :---- |
| **Class** | Each distinct type of label in your classification system. Classes are the buckets that organize your labels. You need at least two classes for any classification task, and each class needs enough examples to teach the system what belongs in that category. | If classifying defects, your classes might be "Scratch," "Contamination," "Void," and "Pass" |
| **Class Taxonomy** | The complete hierarchical structure of all possible classes in your classification system, defined in classes.json. This cannot be changed after dataset creation. | Your defect taxonomy might include top-level classes like "Physical Defects" and "Contamination," each with specific sub-types |
| **Confidence Score** | A numerical measure (0-100%) indicating how certain the system is about an automatically assigned label. Higher scores mean greater certainty. | An image labeled "Scratch" with 95% confidence versus one with 60% confidence |
| **Dataset** | A collection of images and their associated metadata organized for analysis and labeling. A dataset can contain thousands of images from one or more AOI output directories. | All inspection images from a production run of Product X across multiple scans |
| **Embedding** | The technology that enables Visual Layer to find visually similar images and automatically label thousands from just a few examples, dramatically reducing manual labeling work. | Visual Layer analyzes your images to understand visual patterns, allowing it to recognize that Image A looks more like your "Scratch" seeds than your "Void" seeds |
| **Ground Truth** | Verified, accurate labels that serve as the authoritative reference for training and evaluating machine learning models. Ground truth is established through expert review and validation, providing the foundation for measuring model accuracy and performance. In Visual Layer, your seed examples and reviewed labels form the ground truth for label propagation. | A set of 100 manually verified defect images where domain experts have confirmed each label, used to measure how accurately your model classifies new images |
| **Iteration** | A complete cycle of seed selection, automatic labeling, review, and refinement. Running multiple iterations improves labeling accuracy over time. | First iteration: provide seeds and review results. Second iteration: adjust seeds based on results and review again |
| **Job/Production Metadata** | The production configuration parameters that define how inspection was performed. All folders in a dataset must share the same Job, Setup, and Recipe to ensure consistent scanning conditions. | Job: "Product-X-2025", Setup: "Standard-Inspection", Recipe: "High-Resolution-Scan" |
| **Label** | The category or classification assigned to a single image. Think of it as the answer to "what type is this?" for one specific data point. A label is an instance of a class. | This particular image is labeled "Scratch" (the label is the specific assignment to this one image) |
| **Label Propagation** | A semi-supervised learning process that combines automated pattern recognition with human oversight to label large datasets efficiently. The system learns from your seed examples, automatically assigns labels based on confidence scores, and generates review batches of uncertain images for your verification. Each iteration refines the model as you approve or correct labels, creating a feedback loop that improves accuracy until the system can label independently. | After providing 10 seed examples of "Void" defects, the system automatically labels 800 similar images with high confidence, sends 100 uncertain images for your review, then uses your feedback to relabel and improve accuracy in the next iteration |
| **Metadata** | Descriptive information about your images and inspection process, stored in db.csv and db_export_\*.json files. Includes production parameters, timestamps, and file locations. | Information like scan date, machine ID, product type, and image file paths |
| **Seed** | The initial labeled examples you provide for each class. These training examples show the system what each class looks like in practice. Seeds are the foundation that makes automatic labeling possible. Without good seed examples, the system won't know what patterns to look for. | Selecting 5-10 clear images of scratches to teach the system what "Scratch" defects look like |