# Create & Prepare: Upload & Build {#creating-datasets-from-machine-output}

This section guides you through creating datasets in **Visual Layer** from one or more AOI machine output directories derived from the same production job. 

You'll: 

- choose and upload output folders from your machines for Visual Layer validation 
- select the folders relevant for one specific dataset 
- confirm and wait for Visual Layer to generate the dataset

**Process:**

**To create a dataset**

1. From **Dataset Inventory** (the "Home" page) click **New Dataset.**

   The **Data** area loads.

2. From the **Enter Folder Paths** area, enter only the name of the relevant folder you want to upload.

  
> **Note:**  
> 
  The base path to your machine output is configured during installation. Enter only the folder name.
  

   
   
   ![](images/vl-create-dataset-onprem.png)
   
**Create a New Dataset**

   

3. You can upload additional folders at the same time, or one at a time. To add an additional folder, click **+**.

   An additional field appears for another folder name. Add as many as you need.

4. Click **Add** to add the folder/s to the list.

   **Visual Layer** extracts metadata and validates folder structure and contents. When complete, the folders appear in the **Selected Folders** table.

   
   
   ![](images/vl-create-dataset-selectfolders.png)
   
**Selected Folders table**

   

   The table displays the following information for each folder:

   
   
   
   **Column** & **Description** \\
   
   **Job Name** & The production job identifier from the folder metadata \\
   
   **Setup Name** & The setup configuration identifier from the folder metadata \\
   
   **Recipe List** & The recipe name(s) used during inspection \\
   
   **Image Count** & Total number of images contained in the folder \\
   
   
   

5. All folders in a dataset must share identical Job Name, Setup Name, and Recipe List. **If you uploaded multiple folders and need to identify which are compatible, use the table filters:**

   * **Filter by production metadata** - Use the Job Name, Setup Name, and Recipe Name filters to find folders from the same production run:

      ![](images/vl-create-dataset-selectfolders-filters.png)

   * **Check compatibility** - Hover over the info icon to view details about any incompatible folders:

      ![](images/vl-create-dataset-selectfolders-error.png)

6. Select the folders to be included in the dataset that you're creating.

   Once you select one folder from the list, **Visual Layer** validates compatibility across all folders to ensure they originate from the same production run. Folders with different metadata than the first folder you check are automatically disabled and grayed out. To see those folders again, uncheck any checked folders.

7. Click **Continue**.

   **Visual Layer** loads a preview of the intended dataset (a combination of all of the folders you selected) for you to review and approve.

   
   
   ![](images/vl-create-dataset-preview.png)
   
**Preview Dataset**

   

8. Click **Create Dataset**.

   **Visual Layer** begins processing the dataset.

   
   
   ![](images/vl-create-dataset-progress.png)
   
**Creation Progress steps**

   

   Processing time varies with dataset size, typically 5-15 minutes for standard production runs. When complete, you'll receive a notification.