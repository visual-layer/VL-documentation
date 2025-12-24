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

