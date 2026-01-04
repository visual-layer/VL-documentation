# Create & Prepare: How It Works {#how-dataset-creation-works}

Creating a dataset is the first main step in the **Visual Layer** workflow for curating your data and labeling images.

 

> **Note:**  
> 
Multiple folders must share identical Job/Setup/Recipe to be combined. This structure is required in order to ensure that in any given dataset, only outputs from the same production job are included.

You can quickly create and prepare a dataset for label propagation as outlined in the following diagram:

![](images/vl-create-prepare-flow-diagram.png)

**Dataset Creation & Preparation Workflow**

| **Step** | **Phase** | **Description** |
| --- | --- | --- |
| ![](images/1light.png) | **Upload & Select Folders** | Browse and upload AOI output directories that you want to include in the dataset. Upload as many as you'd like. For each folder, **Visual Layer** then automatically validates required files. |
| ![](images/2light.png) | **Build & Create** | From the list of uploaded folders, checkmark all the folders to be included in the dataset. **Visual Layer** then creates the dataset, indexing and clustering images, and loading your class taxonomy based on the information that was included in each uploaded folder from Camtek. |
| ![](images/3light.png) | **Explore Dataset** | When the [dataset is ready](#dataset-creation-stages), explore the dataset to identify representative examples for each defect class. |
