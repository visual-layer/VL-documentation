# Add Media to Datasets {#adding-media-to-datasets}

  As production continues, inspection machines continuously generate new data. New images may contain defects you're already tracking, introduce entirely new defect types, or
   present a combination of both.

  You can add these images to existing datasets without creating new ones. This maintains dataset continuity across production runs and preserves your existing class
  taxonomy. After re-indexing, you can re-run label propagation on the complete dataset, reusing your proven seed examples while Visual Layer learns from both existing and
  newly added images together.

  Adding media to an existing dataset enables you to:

* Expand training datasets with new production examples without fragmenting data across multiple datasets
* Maintain consistent Job Recipe and class taxonomy across all images in a dataset
* Continue [label propagation](#re-indexing-the-updated-dataset) workflows on newly added images using existing seed examples and model learning
* Track dataset evolution over time while preserving the original dataset ID and configuration

## How It Works

**Visual Layer** uses a two-stage process when adding media to optimize performance and give you control over when computationally intensive operations run. New media becomes immediately visible for [exploration](#adding-media-to-an-existing-dataset) after upload. You'll trigger indexing **separately** when you're ready. 

---

**Here's how it works:**

| **Step** | **Phase** | **Description** |
| --- | --- | --- |
| ![](images/1light.png) | **Upload and Validate** | Upload new AOI output folders. **Visual Layer** validates that the metadata matches the existing dataset exactly. |
| ![](images/2light.png) | **Partial Update** | **Visual Layer** automatically generates embeddings for visual search, creates thumbnails, processes metadata, and groups new images into a temporary "New Media" cluster visible immediately for exploration. This cluster is part of your existing dataset, but separate from all other clusters during this stage, enabling you to review the added media before re-indexing completely. Additionally, you can repeat these steps to continue adding additional folders if you didn't include all relevant media initially. When this update is complete, all media that was newly added is in **Pending Indexed** status. |
| ~ |
| ![](images/3light.png) | **Manually Trigger Re-indexing** | When ready, you can trigger full indexing. During indexing, **Label Propagation** is unavailable. **Visual Layer** re-clusters all images (new and existing), regenerates quality issue detection, and updates cluster IDs. Dataset status changes to **Indexing**. |
| ![](images/4light.png) | **Ready for Use** | Indexing completes and dataset status returns to **Ready** status. All media in the datset is set to **Indexed** status. New images are fully integrated in the dataset, with all clusters refreshed accordingly, and available for label propagation and training. |

> **Note:**  
> 
Dataset ID and all image IDs remain unchanged during indexing. Only cluster IDs are updated to reflect the new clustering results.

## Adding Media to an Existing Dataset {#adding-media-to-an-existing-dataset}

Visual Layer uses a two-stage process when adding media to optimize performance and give you control over when computationally intensive operations run. New media becomes immediately visible for [exploration](#adding-media-to-an-existing-dataset) after upload, with full indexing triggered manually when you're ready. You can upload multiple batches and explore before triggering the clustering and analysis steps.

> **Critical:**  
> 
New media must match the metadata of the original dataset. Mismatched metadata will cause validation failures and prevent media from being added. 

To work with datasets that have different metadata, [create a new dataset](#creating-datasets-from-machine-output) instead.

> **Note:**  
> 
If you encounter validation errors, see [Troubleshooting Common Issues](#troubleshooting-common-issues) in the **Appendices** for required file specifications and common error solutions.

**Process:**

**To add media to an existing dataset**

1. Navigate to the dataset where you want to add new images.

2. Go to the **Data** tab.

    The **Data** area loads, similar to the following:

    
    
    ![](images/vl-dataset-updatedataset.png)
    
**Data Tab for Adding Media**

    

    This tab uses the same interface as [dataset creation](#creating-datasets-from-machine-output), but adds media to the current dataset instead of creating a new one. The original folder/s you used to create the dataset appear in the **Select Folders** table, and you can add additional folders as well.

    The name of the dataset you're updating appears at the top left accordingly. Hover over the ![](images/vl-info-i-icon.png) next to the dataset name to confirm its details:

    
    
    ![](images/vl-dataset-updatedataset-i-icon-hover.png)
    
**Dataset Details Tooltip**

    

3. Click **Browse Folders** and select your AOI output folder containing the new images and metadata files.

   
> **Note:**  
> 
   You can add multiple folders to a single dataset, as described in the next step.
   

4. **Visual Layer** extracts metadata and validates folder structure and contents.

   When complete, the folder appears in a table on the same screen.

5. Upload additional folders that share identical metadata with the original dataset.

      
> **Tip:**  
> 
      If you have multiple production runs to add, upload them all before triggering indexing. This reduces processing time and ensures the clustering algorithm analyzes your complete dataset together.
      

   **Visual Layer** validates Job/Setup/Recipe compatibility against the existing dataset to ensure all folders originate from the same production run.

   ![Selected Folders table](images/vl-create-dataset-selectfolders.png)

6. Folders appear in the table showing their compatibility status:

   
> **Note:**  
> 
   See [Creating a Dataset](#creating-datasets-from-machine-output) for additional details.
   

7. Filter the **Selected Folders** table to identify compatible folders:

      Since you may not know the folder origins in advance, upload as many folders as relevant and then use the table filters to identify those that share identical Job/Setup/Recipe metadata with the existing dataset.

      * **Filter by production metadata** - Use the Job Name, Setup Name, and Recipe Name filters to identify folders from the same production run:

         ![](images/vl-create-dataset-selectfolders-filters.png)

      * **Check compatibility** - Hover over the info icon to view details about any incompatible folders:

         ![](images/vl-create-dataset-selectfolders-error.png)

      Compatible folders remain selectable, while incompatible folders (those with different metadata) are grayed out and cannot be selected.

8. Mark the folders from the list that should be added to the dataset and click **Continue**.

   
   
   ![](images/vl-dataset-updatedataset-selectfolders-alreadyexists.png)
   
**Selected Folders for Adding Media**

   

   **Visual Layer** loads a preview of the intended dataset update for you to double-check and approve.

9. Click **Add Media**.

   
   
   ![](images/vl-create-dataset-progress.png)
   
**Upload Progress steps**

   

10. When upload completes, a notification confirms that new media was successfully added. All newly added media is marked with status **Pending Indexed**, for which you can filter when exploring your dataset: 

   ![Pending Indexed](images/vl-addmedia-pendingindexed.png)

## Re-indexing the Updated Dataset {#re-indexing-the-updated-dataset}

After reviewing your new clusters, you can re-index the entire dataset in order to commence a new [label propagation](#re-indexing-the-updated-dataset) round.

1. When ready to proceed with [label propagation](#re-indexing-the-updated-dataset) or [training](#train), click **Re-Index Dataset**. If you plan to add more media, wait and batch multiple uploads before indexing.

   Full indexing begins. The dataset status changes to **Indexing**, and the following features become temporarily unavailable: **Label Propagation** and **Adding Media**.

   
> **Note:**  
> 
   Track indexing progress in the **[Task Manager](#task-manager-statuses)**, which shows task type, dataset name and ID, duration, and status.
   

2. When indexing finishes, a notification appears confirming the dataset is ready.

   All features are re-enabled. Your newly added images are now fully integrated and available for [label propagation](#re-indexing-the-updated-dataset) and [training](#train).

## Updating Dataset Labels

Once the dataset has been reindexed, you can return to [label propagation](#re-indexing-the-updated-dataset). Assuming the labels you initially used are still relevant for images in the dataset, we recommend you approach this as follows:

1. From inside the relevant dataset, initiate [label propagation](#re-indexing-the-updated-dataset), adding all of the relevant class labels. 

   This includes any new labels that may now be relevant!

2. Filter for all of your original seed images for one of the relevant labels. 

3. Select one, and then choose **Select All**. 

3. Add them to the relevant label in the right panel. 

4. Repeat the process for all other labels that you already identified seed examples for. 