# Label Propagation: How It Works {#how-label-propagation-works}

Label propagation is a semi-automated labeling process that transforms visual data annotation from a one-time task into a continuous improvement cycle. **Visual Layer** first receives instructions and human oversight to teach the system which labels to apply and for what kinds of images, combining automated pattern recognition with human oversight to create a feedback loop where each iteration improves labeling accuracy. 

This feedback loop gives the system the guidance necessary in order to guarantee near-perfect automatic labeling thereafter.

> **Note:**  
> 
Each dataset maintains its own independent model, preventing cross-contamination between production runs. 

![](images/vl-labelpropagation-workflow-diagram.png)

**Label Propagation Workflow**

---

**The label propagation process includes these substeps:**

| **Step** | **Phase** | **Description** |
| --- | --- | --- |
| ![](images/1light.png) | **Seed Creation** | Provide ≥5 examples per class to teach the system what each class looks like. |
| ![](images/2light.png) | **Iterative Review Cycle** | Work with **Visual Layer** to refine labels:
- The system automatically labels high-confidence images
- Uncertain images are sent to you in small review batches
- You review and provide feedback on these batches
- The system learns and improves with each review round |
| ![](images/3light.png) | **Automatic Completion** | When model confidence reaches the threshold, label propagation automatically completes and applies final labels to the entire dataset. |
