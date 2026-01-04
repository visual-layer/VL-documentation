# Label Propagation: Review & Iterate {#reviewing-and-providing-feedback}

After submitting seeds, label propagation enters the iterative review cycle. 

**Visual Layer** uses a confidence-based approach that creates review batches when it's uncertain about image classifications. This process ensures labeling accuracy while maintaining efficiency and continues until the model reaches sufficient confidence across your dataset. The system assigns confidence scores to each image for every possible class, creating targeted review batches for human verification.

| **Step** | **Phase** | **Description** |
| --- | --- | --- |
| ![](images/1light.png) | **Confidence Scoring** | After analyzing your seed examples, **Visual Layer** assigns confidence scores (0--100\%) to each image for every possible class. |
| ![](images/2light.png) | **Automatic Labeling** | Images with high confidence scores (typically 90\% or higher) are automatically labeled and do not require review. |
| ![](images/3light.png) | **Review Batch Creation** | Images with low confidence scores are sent to review batches. Each review round includes a maximum of 5--10\% of your total dataset. Example: with 1,000 images, you review approximately 50--100 images. |
| ![](images/4light.png) | **Human Feedback** | Label propagation pauses and waits for your feedback. The process does not continue until the entire review batch is completed. Review automatically generated labels, especially items flagged for attention. You approve, correct, or reassign labels for uncertain images. Your feedback directly improves model accuracy in subsequent iterations. |
| ![](images/5light.png) | **Refinement** | **Visual Layer** incorporates feedback and relabels the dataset with improved accuracy. This cycle repeats, generating new review batches as the model refines its understanding. |

### Source Indicators

| **Icon** | **Source** | **Description** |
| --- | --- | --- |
| ![](images/vl-labelpropagagtion-metadata tags-vl) | **VL** | Label assigned by **Visual Layer** with high confidence |
| ![](images/vl-labelpropagagtion-metadata tags-user) | **User** | Label reviewed and confirmed by you in previous iterations |
| *(no icon)* | **Seed** | Original examples you provided during seed creation; **seed** is separated from **user** because seed-assigned labels cannot be edited later |

> **Tip:**  
> 
All VL and User items remain editable regardless of source. Previous review decisions can be corrected if needed.

### Feedback Actions {#feedback-actions}

During review rounds, you can provide feedback to the system via the feedback actions: 

   ![Feedback Options](images/vl-labelpropagation-review-bar.png)

---

Following are the feedback actions and how to use each:

| **Action** | **Use Case** | **What Happens** | **Important Notes** |
| --- | --- | --- | --- |
| -0.7![](images/vl-remove-redx-icon.png) | **Incorrect (Reject)** | Certain it's wrong class, unsure of which label is correct | Item moves to next-best predicted class
    Remains flagged ``Requires Review''
    Can continue rejecting until right class found | Undo available via toast notification
    Example: Unknown defect types cycle through suggestions until recognized |
| -0.7![](images/vl-ignore-icon.png) | **Ignore** | Outlier that doesn't match any existing class | Item excluded from label propagation
    Placed in ``Unlabeled'' cluster
    Appears grayed out
    Does not count toward progress | System maintains 5–10\% review quota
    Too many ignored items may trigger additional review batches |
| -0.7![](images/vl-approve-icon.png) | **Approve** | Item correctly matches assigned class | Green border indicates approval
    Advances to next item | Confirms model prediction |
| -0.7![](images/vl-labelpropagation-assigndifferentlabel-icon.png) | **Assign to Other Class** | Assign to a different existing class | Manually reassigned to selected class
    Advances to next item | Directly teaches model correct classification |

> **Important:**  
> 
1. Items are organized by their suggested class based on highest confidence score. 
2. You can provide feedback on both review items and high-confidence items (marked Annotated). 
3. All feedback helps improve subsequent labeling iterations.

### Progress Indicators {#monitoring-progress}

Throughout the label propagation process, **Visual Layer** displays progress indicators that track your advancement toward training readiness (minimum 100 labeled images per class) and overall dataset completion. These indicators help you understand when you've met the requirements to train models and make informed decisions about when to finish label propagation.

See [Progress Indicators](#progress-indicators-reference) in the **Appendices** for detailed descriptions and examples of each progress indicator.

**Process:**

**To start a review round**

1. When a review batch is ready for your review, a notification appears in the interface:

   
   
   ![](images/vl-labelpropagation-needsreview-notification.png)
   
**Review Batch notification**

   

   The labeled images are automatically grouped by predicted class/label.

2. Click **Review** to begin reviewing images that were automatically labeled by **Visual Layer**.

   
> **Note:**  
> 
   During review, all exploration features like filters, search, and visual similarity are disabled.
   

   **Visual Layer** automatically loads one of the clustered classes for review. The view displays all images that were assigned the same predicted label, grouped together for efficient review:

   
   
   ![](images/vl-camtek-labelpropagation-reviewround-firstset.png)
   
**Review Round - First Class Loaded**

   

   You can search for specific classes if you have many classes to review:

   
   
   ![](images/vl-review-search-classes.png)
   
**Search classes**

   

   Within each class, you can switch between two tabs:

   * **For Review** (default tab) - Displays images that need your review, marked with ![Requires Review badge](images/vl-labelprop-label-forreview.png). 

   * **Annotated** - Displays seed samples you provided and images that **Visual Layer** labeled with high confidence (typically ≥90%). All items are marked with ![Annotated badge](images/annotated-badge.png) and show their source indicator (VL for automated labels, User for reviewed items, or Seed for original examples).

   
   
   ![](images/vl-camtek-labelpropagation-reviewround-firstset-annotated.png)
   
**Annotated Tab View**

   

   You can also view all clusters included in the propagation, similar to other cluster views in **Visual Layer**. Each cluster card displays:

   * Total number of images in the cluster for this review round (including both Annotated and For Review images)
   * Number of **For Review** images specifically for that cluster

   
   
   ![](images/vl-camtek-labelpropagation-reviewround-allclusters.png)
   
**All Clusters View**

   

   
> **Note:**  
> 
   If a class has no images for review in the current round, its cluster card appears but shows no content, as seen with "Bump Scratch" in the example above.
   

3. Review every image for every class:

   * Provide feedback directly from the default display.
   * Alternatively, double-click any image to open a modal carousel view.

     
     
     ![](images/vl-review-carousel-modal.png)
     
**Carousel Modal**

     

   * Navigate through individual items using carousel controls.
   * Zoom in/out for detailed defect inspection.
   * Click a label from the right side to apply a different label than was initially applied.

4. For every automatically labeled image, provide the model with feedback:

   * Approve
   * Reject
   * Ignore
   * Apply different label

   See [Feedback Actions](#feedback-actions) for more information.

5. Review each item in every class until all items are processed.

6. Click **Submit** to send all your feedback to the system. Label propagation continues with the next iteration, using your feedback to improve accuracy in subsequent labeling cycles. When the system has high confidence, it automatically applies labels during the relevant cycle. 

7. Once the system is confident and applies all labels across your entire dataset, a notification pops up, similar to the following: 

   
   
   ![](images/vl-labelpropagation-complete-notification.png)
   
**Propagation Success**

   

## Managing Iterations and Completion {#managing-iterations-and-completion}

This section outlines how to manage the lifecycle of a label propagation run after seed creation and initial labeling:

* finishing the run early to finalize labels
* resetting the process if the results are unsatisfactory

### Finish Label Propagation Early

Once the system is confident and applies all labels across your entire dataset, a notification pops up.

You can finish the process early, enabling Visual Layer to apply labels across your dataset before completing all iterations. This is available when **Needs Review** status is active only.

![Finish Early](images/vl-labelpropagation-review-finish-panel.png)

From the review details in the right panel:

1. Click **Finish** when satisfied with current progress.
2. Confirm the action in the dialog that appears.

   The system:
   
   * Stops label propagation immediately
   * Writes all labeled data permanently to your dataset
   * Leaves remaining unlabeled data unchanged

### Resetting the Process

You can reset the process only during **Review** stages. Reset **_permanently deletes_** all label propagation progress and cannot be undone. Your original dataset and any labels from previous completed label propagation runs remain unchanged.

Reset label propagation if you:

* notice consistent labeling errors that suggest poor seed examples
* want to try a different class taxonomy or seed strategy
* the results are not meeting your accuracy expectations
* accidentally started with incorrect seed examples

**Process:**

**To reset the process**

> **Critical:**  
> 
Reset **_permanently deletes_** all label propagation progress and cannot be undone. Your original dataset and any labels from previous completed label propagation runs remain unchanged.

1. From the right panel, click ![](images/vl-reset-button.png).
2. Confirm the reset action in the warning dialog.
3. The system completely deletes all:
   * automatically labeled images (high-confidence assignments)
   * user review feedback and corrections
   * progress and iteration history

## Next Steps

When your dataset reaches train-worthy status, it's time to [train your downstream models](#train). 
Alternatively, you can [evaluate labeling results](#evaluating-label-propagation).