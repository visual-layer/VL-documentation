# Train Models: Initiate {#train}

Once your dataset reaches train-worthy status with at least 100 labeled images per class, you can initiate model training to send your labeled data to the Camtek training infrastructure.

**Process:**

**To initiate model training**

1. Navigate to the relevant dataset.

2. Click ![](images/vl-train-model-button.png) in the top right corner. The **New Auto Training Job** dialog opens, similar to the following:

   
   
   ![](images/vl-labelpropagation-new-training-downstream.png)
   
**Training Job dialog**

   

   Following are details of the fields in this window:

| **Component** | **Description** | **Example/Notes** |
| :---- | :---- | :---- |
| **Dataset Name** | The human-readable name of the **Visual Layer** dataset being sent for training. | Populated automatically from the current dataset. (Read-only, for reference); you can change the name from the title bar inside the dataset itself. |
| **Dataset ID** | The unique system identifier for the dataset. | For example: 0f4698-9940-11f0-8218-6ad3b2ffe3e5 (Read-only, for reference) |
| **Model Name** | Allows selection of the target Camtek model configuration for this training run. The available models are automatically retrieved from your Camtek training infrastructure. | Select from the dropdown list of models configured in your Camtek environment. |
| **Train button** | Initiates the training job. | Click to package the labeled data and send it to the Camtek training infrastructure. |

3. From **Model Name** choose the relevant model.

4. Click **Train**.

   
   
   ![](images/vl-labelprop-trainmodel-datasetsentsuccessfully.png)
   
**Training Success**

   

   **Visual Layer** automatically packages your labeled dataset with all metadata and sends it to your training infrastructure.

5. Monitor the training progress, which appears in the action bar:

   
   
   ![](images/vl-trainmodel-progress.png)
   
**Training Progress indicator**

   

   **Visual Layer** provides real-time progress updates showing the current status and completion percentage (0-100%). If training fails, hover over the status to view error details. See [Model Training Statuses](#training-status-reference) in the Appendices for descriptions of all training stages.

   Training typically completes within several hours depending on dataset size and model complexity.

**Process:**

**After training completes**

When model training finishes successfully, Camtek returns the HTML report path and **Visual Layer** marks the model as **Completed** in the [**Model Catalog**](#the-model-catalog). A success notification appears: **Your model has been created successfully. You can explore it in the Model Catalog.**

Click **View Model** to navigate directly to the [**Model Catalog**](#the-model-catalog) where your new model will be highlighted and auto-scrolled into view.