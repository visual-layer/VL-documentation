# Label Propagation: Add Seeds {#seed-creation}

To get started with label propagation you'll provide **Visual Layer** with seed examples that train our system to automatically label your remaining data. Label propagation can run on either the entire dataset or a subset, for example newly added data only.

> **Important:**  
> 
1. **Visual Layer** assigns a single label to each image during label propagation. Multi-label classification is not supported. 
2. Starting label propagation over from scratch **__replaces__** all previous label propagation results—existing labels are overwritten and cannot be recovered. 
3. After finalizing label propagation, labels cannot be edited without running a new label propagation iteration.

> **Note:**  
> 
During seed creation, only class assignment is available and other exploration features are disabled.

**Process:**

Best practices

To maximize success with label propagation:

| **Best Practice** | **Description** |
| :---- | :---- |
| **Plan Your Classes** | Select ≥2 classes. Include every class that may appear—classes cannot be added later. |
| **Provide ≥5 Examples Per Class** | Minimum required to proceed. More diverse examples = better accuracy. |
| **Choose Representative Examples** | Select clear, typical instances showing the full visual range of each class. Avoid edge cases or ambiguous images. |
| **Triple-Check Before Starting** | Seed examples cannot be edited once propagation begins. Verify all assignments are correct. |

**Process:**

**To prepare your dataset**

1. Navigate to the relevant dataset in **Visual Layer**.

2. From the panel on the right side, click ![](images/vl-labelpropagation-tab-icon.png).

   The **Label Propagation** tab loads.

   
   
   ![](images/vl-labelpropagation-tab.png)
   
**Label Propagation Tab**

   

3. To start, you need to select all of the class labels that are relevant for the dataset.

   Click ![](images/vl-labelpropagation-chooseclasses.png)

   The **Add Labels** dialog pops open:

   
   
   ![](images/vl-labelpropagation-addlabels.png)
   
**Add Labels dialog**

   

4. Click in the field and choose labels from the dropdown list.

   
> **Important:**  
> 
   You must select ***at least two classes*** for which you'd like to prepare labeling; classes not defined during this process cannot be assigned. 
   

   Select all classes that appear in your dataset. This is important because the system will attempt to label all data.

   
> **Note:**  
> 
   This list contains the predefined classes from the `classes.json` file provided by your AOI machine and loaded during [dataset creation](#creating-datasets-from-machine-output). 
   

   
5. Click **Add**.

   The label classes appear in the right panel.

6. For each class label, select a minimum of 5 seed examples:

   * **Drag and Drop** - For a single image or for a single cluster (in its entirety), drag it directly into the designated class area with visual feedback provided OR,

   * **Select & add** - Select all relevant images and then from the floating bar choose the relevant class and click **Assign Label**:

   ![Assign Label button](images/vl-labelprop-assignlabel.png)

   Each class shows a preview of the examples that you assigned.

   
      
      ![](images/vl-labelpropagation-seed-examples-preview.png)
      
**Seed Examples preview**

   

5. Review and refine your selections:

   * To remove an example, hover over it and click ![Remove Example icon](images/vl-labelpropagation-deleteremove-labelclass-icon.png).

   * Visual indicators show when you've met the minimum 5 examples per class requirement. See [Progress Indicators](#progress-indicators-reference) in the **Appendices** for details on all progress tracking.

   * To manage classes as needed during the seed creation process, click **Add Labels** to add additional classes for propagation.

   * Click ![Remove example icon](images/vl-labelpropagation-deleteremove-labelclass-icon.png) from the row with the class name to delete the entire sample set (and the label) from propagation.

6. When ready, click **Submit**.

   
   
   ![](images/vl-labelpropagation-runningspinner.png)
   
**Label Propagation Running**

   

   **Visual Layer** analyzes your seed examples and begins labeling images, creating sample sets for each of the class labels you configured.

   The system assigns confidence scores to each image for every possible label. Images with high confidence scores, typically 90% or higher, are automatically labeled ([Annotated](#reviewing-and-providing-feedback)). Images with low confidence scores are sent to review batches for your input ([For Review](#reviewing-and-providing-feedback)). When complete, a notification for review appears in the interface:

   
   
   [t]{0.4}
   
   ![](images/vl-review-batch-notification.png)
   
**Review Notification**

   
   
   [t]{0.4}
   
   ![](images/vl-labelpropagation-progressbars.png)
   
**Progress & Review**

   
   

**Process:**

**Next Steps**

When you receive notification, it's time to [review](#reviewing-and-providing-feedback) the labels added by **Visual Layer**, and continue providing feedback to prepare the system for automated propagation.

