\appendixdivider{Appendices}

\appendix

# User Interface Reference

This reference guide provides detailed descriptions of all **Visual Layer** screens, components, and interface elements. Use this section to understand what each field, button, and area of the platform does.

## Home Page: Dataset Inventory {#dataset-inventory}

!include markdown/snippets/dataset-inventory-landing.md

The home page layout consists of:

\renewcommand{\arraystretch}{1.5}
\rowcolors{1}{tableprimary}{tablesecondary}

\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{4em}|p{0.35\textwidth}|X|}
\hline
\textbf{Area} & \textbf{Name} & \textbf{Description} \\
\hline

\raisebox{-7pt}{\includegraphics[width=6mm]{images/1light.png}}
  & \textbf{Navigation Panel}
  & Navigate to: this area (the \textbf{Dataset Inventory}, which is your \textbf{Home} page), the \textbf{Task Manager}, the \textbf{Model Catalog}, and log in/log out \\
\hline

\raisebox{-7pt}{\includegraphics[width=6mm]{images/2light.png}}
  & \textbf{Main Panel}
  & Search for datasets. \\
\hline

\raisebox{-7pt}{\includegraphics[width=6mm]{images/3light.png}}
  & \textbf{Dataset Inventory}
  & This is your default Home page, as appears in the example above. The \textbf{Dataset Inventory} page displays a complete list of your datasets. Click any dataset to open it. \\
\hline

\raisebox{-6pt}{\includegraphics[width=6mm]{images/4light.png}}
  & \multicolumn{1}{m{0.35\textwidth}|}{%
        \includegraphics[width=4cm]{images/create-dataset-create-button.png}%
    }
  & Create a new dataset. \\
\hline
\end{tabularx}

### Navigation Panel {#nav-panel}

The **Navigation Panel** provides access to all major areas of **Visual Layer**:

\renewcommand{\arraystretch}{1.5}
\rowcolors{1}{tableprimary}{tablesecondary}

\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{4em}|p{0.35\textwidth}|X|}
\hline
\textbf{Icon} & \textbf{Name} & \textbf{Description} \\
\hline

\raisebox{-6pt}{\includegraphics[width=6mm]{images/dataset-inventory-icon.png}}
  & \textbf{Dataset Inventory}
  & A complete list of your datasets. \\
\hline

\raisebox{-6pt}{\includegraphics[width=6mm]{images/task-manager-icon.png}}
  & \textbf{Task Manager}
  & Monitor and manage all active tasks, jobs, and processing workflows. \\
\hline

\raisebox{-6pt}{\includegraphics[width=6mm]{images/modelcatalog-icon.png}}
  & \textbf{Model Catalog}
  & Browse, deploy, and manage trained models for inference and analysis. \\
\hline

\raisebox{-6pt}{\includegraphics[width=6mm]{images/avatar-icon.png}}
  & \textbf{Your Avatar}
  & Log out of your account. \\
\hline
\end{tabularx}

### Dataset Inventory View

The **Dataset Inventory** displays all datasets as cards:

![](images/dataset-inventory-view.png)

![](images/dataset-inventory-cards.png)

#### Dataset Card

Each dataset card appears with a similar layout to the following:

\begin{figure}[H]
\centering
\includegraphics[width=0.4\textwidth]{images/dataset-inventory-card.png}
\caption{Dataset Card Example}
\end{figure}


Each dataset card shows:

| **Field** | **Description** |
| :---- | :---- |
| **Dataset Name** | The title of the dataset for easy identification and reference. |
| **Creation Date** | The date when the dataset was created and added to your inventory. |
| **Dataset Status** | Current state of the dataset shown with status badges. See [Dataset Inventory Statuses](#dataset-inventory-statuses) for complete list. |
| **Image Count** | Total number of images contained in the dataset. |
| **Info Icon** ![](images/info-i-icon.png){ width=3% } | Hover to view associated Job Name, Setup Name, and Recipe Names. |
| **Three-Dot Menu** | Access dataset actions including **Delete**. |

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth]{images/camtek-datasetinventory-metadata.png}
\caption{Dataset Metadata Popup Example}
\end{figure}

### Main Panel Controls

The **Main Panel** appears similar to the following:

![](images/main-nav-panel.png){ width=105% }

The **Main Panel** provides dataset management tools:


| **Control** | **Description** |
| :---- | :---- |
| **Search Bar** | Locate datasets by name. |
| **Filter by Job/Recipe/Setup** | Filter datasets by production metadata (Job Name, Setup Name, Recipe Name). |
| **Sort By** | Arrange datasets based on status, creation date, or other attributes. |
| **Clear Selection** | Reset applied filters. |

## Dataset View

When you open a dataset, the main dataset exploration interface loads:

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{images/overview-cluster-view.png}
\caption{Dataset View with Details}
\end{figure}

The dataset view consists of:

\renewcommand{\arraystretch}{1.5}
\rowcolors{1}{tableprimary}{tablesecondary}

\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}m{4em}|p{0.35\textwidth}|X|}
\hline
\textbf{Area} & \textbf{Component} & \textbf{Description} \\
\hline

\raisebox{-7pt}{\includegraphics[width=6mm]{images/1light.png}} & \textbf{Tabs} & Navigate between Explore, Data and Views. \\
\hline

\raisebox{-7pt}{\includegraphics[width=6mm]{images/2light.png}} & \textbf{Filter Panel} & Apply and combine search criteria. \\
\hline

\raisebox{-7pt}{\includegraphics[width=6mm]{images/3light.png}} & \textbf{Action Bar} & Access operations like exporting. \\
\hline

\raisebox{-7pt}{\includegraphics[width=6mm]{images/4light.png}} & \textbf{Details Sidebar} & View metadata and insights, and access label propagation. \\
\hline

\raisebox{-7pt}{\includegraphics[width=6mm]{images/5light.png}} & \textbf{Thumbnail Grid} & Visual representation of your data in clusters. \\
\hline
\end{tabularx}

### Dataset Metadata

The dataset name appears at the top left of the dataset view. Hover over ![](images/info-i-icon.png){ width=3% } next to the dataset name to view production metadata and confirm dataset details:

\begin{figure}[H]
\centering
\includegraphics[width=0.3\textwidth]{images/dataset-updatedataset-i-icon-hover.png}
\caption{Dataset Details Tooltip}
\end{figure}

Metadata details include: 

| **Field** | **Description** |
| :---- | :---- |
| **Job Name** | The production job identifier from the folder metadata. |
| **Setup Name** | The setup configuration identifier from the folder metadata. |
| **Recipe Names** | The recipe name(s) used during inspection. |

### Cluster View {#clustering-granularity}

**Visual Layer** automatically groups similar images into clusters during dataset creation. Each cluster is displayed as a preview card:

![Cluster preview cards](images/clusters-image-view.png){ width=93% }

From this view, you can see the following details for each cluster: 

| **Cluster Card Element** | **Description** |
| :---- | :---- |
| **Number of items** | The total number of items that match your current filters |
| **Prominent labels** | The most frequent labels within the cluster |
| **Representing images** | Thumbnails of a few key example images that visually summarize the cluster |
| **Visual Similarity Icon** ![](images/visual-similarity-icon.png){ width=7% } | Hover over a cluster to access visual similarity search |

### Filter Menu

Click ![](images/filterbutton.png){ width=6% } from the dataset toolbar:

![All Filters](images/camtek-allfilters.png){ width=40% }

#### Available Filters

| **Filter Category** | **Description** | **Configuration** |
| :---- | :---- | :---- |
| **Folders** | Filter by specific AOI output folders within your dataset | Checkmark the folders to include |
| **Files** | Filter by specific image files or file patterns | Enter filename or pattern to match |
| **Labels** | Filter by assigned labels | Select which labels to include or exclude |
| **User Tags** | Filter by custom tags you've applied to images | Select tags from your tag list |
| **Duplicates** | Show only duplicate or near-duplicate images | Toggle on to show duplicates only |
| **Outliers** | Show images that differ significantly from typical patterns | Toggle on to show outliers only |
| **Quality Issues** | Filter images flagged with quality problems | Select issue types (blur, overexposure, underexposure, etc.) |
| **Select Uniques** | Show only unique images (exclude duplicates) | Toggle on to show unique images only |
| **Insertion Time** | Filter by when images were added to the dataset | Set date ranges for upload time |
| **Media Status** | Filter by processing or indexing status | Select status types (pending, processing, ready, error) |

#### Applied Filters Display

Applied filters appear in the **Query Panel** above the image grid:

![Applied Filters](images/applied-filters.png){ width=80% }

Control filters as follows:

| **Control** | **Description** |
| :---- | :---- |
| **Filter Chip** | Each applied filter shows as a chip with its criteria |
| **X Button** | Click to remove an individual filter |
| **Clear All** | Remove all applied filters at once |

When you apply multiple filters, images must match **all** filter criteria to appear in the results. Within a single filter, you can use available operators (such as selecting multiple folders with OR). However, across different filter types, the criteria combine with AND logic. For example, selecting "Folder A OR Folder B" combined with "Label: Scratch" shows only images from either Folder A or Folder B that are also labeled as Scratch.

### Visual Similarity Search {#visual-search}

**Visual Layer** can find images that look similar to a reference image you provide. This helps you quickly locate all instances of a specific defect type or visual pattern across your entire dataset:

| **Search Method** | **Action** |
| :---- | :---- |
| **From cluster or image in cluster view** | Hover over a cluster or the image and click ![](images/visual-similarity-icon.png){ width=7% } at the bottom of the card. |
| **From the Image Details Page** | Click a single image to open its details page, then click ![](images/visual-similarity-BUTTON.png){ width=30% } from the **Action Bar**. |
| **Using an External Image** | Click ![](images/visual-similarity-searchbaricon.png){ width=8% } near the search bar inside your dataset, upload an image from your device, optionally crop it, and start the search.  |


The visual similarity search analyzes the **entire image content** you provide. If you don't crop, the system will search for images similar to anything and everything visible in your image—including background, borders, and unrelated features. **Always crop to isolate the specific defect or feature** you want to find. This focuses the search on what matters and returns more relevant results.


\processstart
To search using an external image
\processend

1. Click ![](images/visual-similarity-searchbaricon.png){ width=8% } near the search bar inside your dataset.

2. From the popup, browse your local environment or drag and drop an image file.

3. When the image loads, crop it if necessary to focus the search on only part of the image.

4. Click **Find Similar** to start the search.


### Views Tab

The **Views** tab displays saved filter combinations and search queries, allowing you to quickly return to commonly used filter sets without manually reapplying them each time.

**Saving a View**

After applying filters to your dataset, click the **Save as View** button to preserve the current filter combination:

![Save as View button](images/save-view-button.png){ width=60% }

Enter a descriptive, unique name for the view in the dialog that appears:

![Name the View dialog](images/save-view-dialog.png){ width=50% }

**Using Saved Views**

Click any saved view card in the **Views** tab to instantly load its filter combination and see the filtered results.

**Deleting Views**

To delete a view, click the three-dot menu on the view card and select **Delete**. A confirmation dialog appears to prevent accidental deletion:

![Confirm Deletion](images/dataset-views-delete-confirmation.png){ width=60% }

After confirming deletion, a notification confirms the view has been removed:

![Delete Notification](images/dataset-views-delete-notification.png){ width=65% }

Views are immutable. To modify a view, delete it and create a new one with updated criteria.


# Status Reference {#status-reference}

This section provides comprehensive reference information for all statuses displayed throughout **Visual Layer**, including dataset creation stages, dataset operation states, task manager statuses, and model training progress indicators.

**In this section:**

* [Dataset Inventory Statuses](#dataset-inventory-statuses)
* [Dataset Status Indicators (Detail View)](#inside-dataset-statuses)
* [Task Manager Statuses](#task-manager-statuses)

## Dataset Inventory Statuses {#dataset-inventory-statuses}

The **Dataset Inventory** displays status badges on each dataset card, communicating the dataset's current state and operational availability at a glance.

\begin{figure}[H]
\centering
\includegraphics[width=0.8\textwidth]{images/datasetinventory-status-badges.png}
\caption{Dataset Inventory: Dataset Card Statuses}
\end{figure}

The following statuses appear on dataset cards in the **Dataset Inventory**:

\renewcommand{\arraystretch}{2.2}

| **Status** | **Badge** | **Description** |
| :---- | :---- | :---- |
| **READY** | \vspace{2mm}\raisebox{-0.05\height}{\includegraphics[width=0.1\textwidth]{images/statuses/inventory-badge-ready.png}} | No blocking operations are running. All actions are available. |
| **DRAFT** | \vspace{2mm}\raisebox{-0.05\height}{\includegraphics[width=0.1\textwidth]{images/statuses/inventory-badge-new.png}} | Data upload started but **Create Dataset** was not clicked. |
| **UPLOADING** | \vspace{2mm}\raisebox{-0.05\height}{\includegraphics[width=0.15\textwidth]{images/statuses/inventory-badge-uploading.png}} | Dataset upload in progress. |
| **INDEXING** | \vspace{2mm}\raisebox{-0.1\height}{\includegraphics[width=0.15\textwidth]{images/statuses/inventory-badge-indexing.png}} | Dataset indexing and clustering in progress. |
| **ENRICHING** | \vspace{2mm}\raisebox{-0.1\height}{\includegraphics[width=0.15\textwidth]{images/statuses/inventory-status-enriching.png}} | Data enrichment and enhancement in progress. |
| **FAILED** | \vspace{2mm}\raisebox{-0.1\height}{\includegraphics[width=0.15\textwidth]{images/statuses/inventory-badge-failed.png}} | Dataset creation or operation failed. Check error details in notification or **Task Manager**. |
| **UPDATING** | \vspace{2mm}\raisebox{-0.1\height}{\includegraphics[width=0.15\textwidth]{images/statuses/inventory-badge-updating.png}} | A blocking operation is running (Add Media, Label Propagation, or Re-indexing). |
| **PENDING** | \vspace{2mm}\raisebox{-0.05\height}{\includegraphics[width=0.15\textwidth]{images/statuses/inventory-badge-PENDINGINDEX.png}} | New media was added and requires re-indexing. |
| **RESUME** | \vspace{2mm}\raisebox{-0.1\height}{\includegraphics[width=0.15\textwidth]{images/statuses/inventory-badge-resume.png}} | User action is required to complete dataset creation.  |

\renewcommand{\arraystretch}{1}

## Dataset Status Indicators {#inside-dataset-statuses}

When you open a dataset, status indicators appear at the top right corner of the interface. These statuses track processing progress through various stages. When viewing or working with a dataset, the **READY** status indicates all operations are complete and the dataset is available for use.

During initial dataset creation, these statuses are not visible because the dataset doesn't exist yet to open. When [adding media](#adding-media-to-datasets) to an existing dataset, you can navigate inside the dataset and monitor these status indicators as the operation progresses.

The following statuses appear inside the dataset:

\renewcommand{\arraystretch}{1.8}

| **Status** | **Visual Indicator** | **Description** |
| :---- | :---- | :---- |
| **UPLOADING** | \raisebox{-0.5\height}{\includegraphics[width=0.175\textwidth]{images/statuses/dataset-status-uploading.png}} | Upload request acknowledged, data transfer in progress |
| **PRE_PROCESSING** | \raisebox{-0.5\height}{\includegraphics[width=0.175\textwidth]{images/statuses/dataset-status-preprocessing.png}} | Data prepared for indexing and analysis |
| **ENRICHING** | \raisebox{-0.5\height}{\includegraphics[width=0.175\textwidth]{images/statuses/dataset-status-enriching.png}} | Data enrichment and enhancement in progress |
| **INDEXING** | \raisebox{-0.5\height}{\includegraphics[width=0.175\textwidth]{images/statuses/dataset-status-indexing.png}} | Visual indexing and AI-based analysis in progress: learning distribution patterns and creating enhanced embeddings tailored to your data for label propagation accuracy |
| **SAVING** | \raisebox{-0.5\height}{\includegraphics[width=0.175\textwidth]{images/statuses/dataset-status-saving.png}} | Final data save to system in progress |
| **READY** | \raisebox{-0.5\height}{\includegraphics[width=0.12\textwidth]{images/statuses/dataset-status-ready.png}} | Dataset complete and available for exploration |
| **DRAFT** | \raisebox{-0.5\height}{\includegraphics[width=0.12\textwidth]{images/statuses/dataset-status-new.png}} | Dataset creation was started but not completed. Click to resume. |
| **UPDATING** | \raisebox{-0.5\height}{\includegraphics[width=0.175\textwidth]{images/statuses/dataset-status-updating.png}} | A blocking operation is running (**Label Propagation** or **Re-indexing**). Most dataset actions are unavailable until the operation completes. |
| **PENDING** | \raisebox{-0.5\height}{\includegraphics[width=0.15\textwidth]{images/statuses/dataset-status-pending-index.png}} | New media was added and requires re-indexing. |
| **FATAL_ERROR** |  | Irrecoverable failure during dataset creation; check error details in notification or **Task Manager** |

\renewcommand{\arraystretch}{1}


## Task Manager Statuses {#task-manager-statuses}

Tasks are operations you perform in the system, such as creating a dataset, updating an existing dataset or running label propagation. All tasks in the **Task Manager** display one of the following statuses to indicate their current state. Each status includes a percentage to show progress through the operation:

\renewcommand{\arraystretch}{1.8}

| **Status** | **Visual Indicator** | **Description** |
| :---- | :---- | :---- |
| **Initializing** | \raisebox{-0.5\height}{\includegraphics[width=0.13\textwidth]{images/statuses/taskmanager-status-initializing.png}} | The operation is performing initial validations, uploading data, or downloading resources. Progress percentage reflects completion of initialization steps. |
| **Running** | \raisebox{-0.5\height}{\includegraphics[width=0.17\textwidth]{images/statuses/taskmanager-status-running.png}} | The operation is actively processing. Progress percentage reflects completion of the overall operation. |
| **Completed** | \raisebox{-0.5\height}{\includegraphics[width=0.15\textwidth]{images/statuses/taskmanager-status-completed.png}} | The operation completed successfully. Progress shows 100%. |
| **Failed** | \raisebox{-0.5\height}{\includegraphics[width=0.13\textwidth]{images/statuses/taskmanager-status-failed.png}} | The operation encountered an error and could not complete. Hover over the status to view the error message explaining what went wrong. |
| **Aborted** | \raisebox{-0.5\height}{\includegraphics[width=0.13\textwidth]{images/statuses/taskmanager-status-aborted.png}} | The operation was manually stopped by a user before completion. |
| **Waiting for Review** | \raisebox{-0.5\height}{\includegraphics[width=0.18\textwidth]{images/statuses/taskmanager-status-waitingreview.png}} | The label propagation operation completed and is ready for your review. Navigate to the dataset to begin reviewing propagated labels. This status applies only to **Label Propagation** tasks. |

\renewcommand{\arraystretch}{1}

# Troubleshooting Common Issues

This section provides solutions to errors and problems you might encounter while working with **Visual Layer**. Each issue includes an explanation of what went wrong and specific steps to resolve it.

## Dataset Creation and Media Upload Errors

\camtekaoioutput

When uploading folders or adding media to datasets, **Visual Layer** validates that all required files exist and are structured as expected. If validation fails, you'll see one of these error messages:

| **Error** | **What It Means** | **How to Fix** |
| :---- | :---- | :---- |
| **Missing required files** | Your folder is missing one or more required files: db.csv, metadata.json, classes.json, or db\_export\_\*.json | Check that the AOI scan completed successfully. All four file types must be present in the folder. |
| **Invalid file naming** | The db\_export file doesn't follow the expected naming pattern | Rename the file to match the pattern: db\_export\_\[id\].json (for example, db\_export\_12345.json) |
| **JSON parsing error** | The classes.json or db\_export file contains syntax errors | Open the file in a JSON validator to identify and fix formatting issues (missing commas, quotes, brackets, etc.) |
| **Cross-validation failure** | Job Name, Setup Name, or Recipe Name don't match between files within the same folder | The metadata.json file may be corrupted. Try regenerating the scan from the AOI machine. |
| **Job Recipe mismatch** | Job Name, Setup Name, Recipe Name, or Tool List differs between folders you're trying to combine—or doesn't match the original dataset when adding media | For new datasets: Only combine folders from the same production run. For adding media: Ensure the new folder came from the exact same Job/Setup/Recipe as the original dataset. |
| **ImageName mismatch** | Filenames listed in db.csv don't match the actual image files in the folder | Check that the ImageName column in db.csv contains exact filenames with extensions. Fix any typos or missing extensions. |
| **Class taxonomy mismatch** | Class taxonomy is the complete set of label definitions for all categories/types of images that are in a single dataset. The classes.json file defines different classes than the original dataset | When adding media to an existing dataset, you must use the identical classes.json file from the original dataset creation. Classes cannot be changed when adding media. |

## Label Propagation

These issues might arise during seed creation and iterative review. Most problems stem from insufficient or unrepresentative seed examples.

| **Problem** | **Description** | **Resolution** |
| :---- | :---- | :---- |
| Inaccurate results for certain defect types | The system consistently mislabels specific defect types. High-confidence automatic labels are frequently incorrect during review. | Add more diverse seed examples showing the full range of that defect type's visual variations. Avoid using edge cases or ambiguous examples as initial seeds. Reset if needed to start with improved seeds. |
| Cannot drag multiple selected items to assign labels | You're trying to drag multiple selected images to a label, but only single items can be dragged. | Use the Select & Add workflow instead: select multiple images using checkboxes, click **Assign Label**, then choose the target label from the dropdown. |

# Frequently Asked Questions

**Q: Why do review batches keep appearing? How many times do I need to review?**

A: Label propagation is an iterative process where each review round improves the system's accuracy. Continue reviewing until **Visual Layer** reaches high confidence across your dataset or you're satisfied with the labeling progress. The number of iterations varies based on dataset complexity and seed quality.

**Q: Why can't I edit my seed examples after starting label propagation?**

A: Seeds become immutable once propagation begins to ensure consistency throughout the iterative learning process. If you need to change seeds or classes, use ![](images/reset-button.png){ width=15% } to start over. Note that this permanently deletes all label propagation progress but preserves your original dataset.

**Q: What do the source indicators (VL, User badges) mean?**

A: These badges show the origin of each label. ![VL](images/labelpropagagtion-metadata tags-vl.png){ width=9% } means the label was assigned by **Visual Layer** with high confidence. ![User](images/labelpropagagtion-metadata tags-user.png){ width=9% } means you reviewed and confirmed the label in a previous iteration. Seed examples appear without a badge. See [Reviewing and Providing Feedback](#reviewing-and-providing-feedback) for complete definitions.

**Q: Can I run label propagation on the same dataset multiple times?**

A: Yes. However, each new run will overwrite all existing labels in the dataset. To preserve existing labels when running label propagation again (for example, after adding new media), use filters to view images by label, then add all previously labeled images as seed examples for their respective classes before starting the new run. This workflow gives you flexibility to either preserve previous labels or start fresh.

**Q: What happens to images I marked as "Ignore"?**

A: They are excluded from label propagation, placed in an "Unlabeled" cluster, and don't count toward training readiness or review quotas.

**Q: Do I have to start from scrach after updating a dataset with new media?**

No. To preserve existing labels when adding new media, filter by each label, drag those images as seeds for their respective classes, and then start a new label propagation run. See [Updating Dataset Labels](#updating-dataset-labels) for more information.

**Q: Can I export data before reaching "Train Worthy" status?**

A: Yes. You can export **Label Propagation** results at any point using ![](images/export-download-icon.png){ width=5% }, even if you haven't reached the 200 images per class threshold.

**Q: How do I know if my seed examples are good quality?**

A: Monitor first-iteration results. If many high-confidence automatic labels are incorrect during your first review, your seed likely needs improvement. Use ![](images/reset-button.png){ width=15% } and select clearer, more representative examples.

**Q: Can I combine datasets from different Jobs/Setups/Recipes?**

A: No. Each dataset must contain folders with identical Job, Setup, and Recipe metadata. Create separate datasets for different production runs, then filter and organize them using the metadata filters.

**Q: Why are some folders grayed out when I try to add media or create a dataset?**

A: **Visual Layer** automatically validates metadata compatibility. Grayed-out folders indicate their Job, Setup, Recipe, or Tool List metadata doesn't match the other selected folders. Hover over ![](images/info-i-icon.png){ width=3% } to view the specific mismatch. You can either select only folders with matching metadata, or create separate datasets for incompatible production runs.

**Q: How do I fix incorrect seed examples or classes after starting label propagation?**

A: Use ![](images/reset-button.png){ width=15% } to start over with new seeds or classes. This permanently deletes all label propagation progress but preserves your original dataset. Seeds become immutable once propagation begins to ensure consistency throughout the iterative learning process, so resetting is the only way to change them.

**Q: Why haven't I reached train-worthy status after multiple review rounds?**

A: **Visual Layer** requires a minimum of 200 images per class for training readiness. Continue review rounds until this threshold is met. If progress is very slow, verify you have sufficient unlabeled data in your dataset and consider adding more images. The number of iterations needed varies based on dataset size, complexity, and seed quality.


# Terms and Definitions

| **Term** | **Definition** | **Example/Context** |
| :---- | :---- | :---- |
| **Class** | Each distinct category or group of images/defects. | If classifying defects, your classes might be "Scratch," "Contamination," "Void," and "Pass" |
| **Class Taxonomy** | The complete list of label definitions for the defect categories available in your dataset, retrieved from your inspection equipment and defined in classes.json. Once the dataset is created, you cannot add or remove categories. | Your defect taxonomy might include classes like "Scratch," "Contamination," "Void," and "Pass" |
| **Cluster** | A group of visually similar images automatically organized by **Visual Layer**. Clusters help you quickly identify patterns and find similar defects without examining every image individually. | All images showing scratch-like patterns grouped together in one cluster card, making it easier to review similar defects at once |
| **Confidence Score** | A numerical measure (0-100%) indicating how certain the system is about an automatically assigned label. Higher scores mean greater certainty. | An image labeled "Scratch" with 95% confidence versus one with 60% confidence |
| **Dataset** | A collection of images and their associated metadata organized for analysis and labeling. A dataset can contain thousands of images from one or more AOI output directories. | All inspection images from a production run of Product X across multiple scans |
| **Embedding** | A mathematical representation of an image that captures its visual characteristics as a series of numbers. This is the technology that enables **Visual Layer** to find visually similar images and automatically label thousands from just a few examples. **Visual Layer** generates embeddings for every image in your dataset. Images that look similar have similar embeddings, which enables automatic clustering, visual similarity search, and efficient pattern recognition across thousands of images. | Two scratch defects will have embeddings that are mathematically close to each other, while a scratch and a void will have embeddings that are far apart. This similarity measurement powers the automatic grouping of visually similar images into clusters. |
| **Ground Truth** | Verified, accurate labels that serve as the authoritative reference for training and evaluating machine learning models. **Ground Truth** is established through expert review and validation, providing the foundation for measuring model accuracy and performance. In **Visual Layer**, your seed examples and reviewed labels form the **Ground Truth** for label propagation. | A set of 100 manually verified defect images where domain experts have confirmed each label, used to measure how accurately your model classifies new images |
| **Iteration** | A complete cycle of seed selection, automatic labeling, review, and refinement. Running multiple iterations improves labeling accuracy over time. | First iteration: provide seeds and review results. Second iteration: adjust seeds based on results and review again |
| **Job/Production Metadata** | The production configuration parameters that define how inspection was performed. All folders in a dataset must share the same Job, Setup, and Recipe to ensure consistent scanning conditions. | Job: "Product-X-2025", Setup: "Standard-Inspection", Recipe: "High-Resolution-Scan" |
| **Label** | The category name applied to a single image, identifying its type. A label is an instance of applying a class to an image. | This particular image is labeled "Scratch" (applying the "Scratch" class to this specific image) |
| **Label Propagation** | A semi-supervised learning process that combines automated pattern recognition with human oversight to label large datasets efficiently. The system learns from your seed examples, automatically assigns labels, and generates review batches of images that need your verification. Each iteration refines the model as you approve or correct labels, creating a feedback loop that improves accuracy until the system can label independently. | After providing 10 seed examples of "Void" defects, the system automatically labels 800 similar images, sends 100 images for your review, then uses your feedback to relabel and improve accuracy in the next iteration |
| **Metadata** | Descriptive information about your images and inspection process, stored in db.csv and db\_export\_\*.json files. Includes production parameters, timestamps, and file locations. | Information like scan date, machine ID, product type, and image file paths |
| **Seed** | The initial labeled examples you provide for each class. These training examples show the system what each class looks like in practice. Seeds are the foundation that makes automatic labeling possible. Without good seed examples, the system won't know what patterns to look for. | Selecting 5-10 clear images of scratches to teach the system what "Scratch" defects look like |
