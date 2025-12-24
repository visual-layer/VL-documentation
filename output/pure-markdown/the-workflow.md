# The Workflow: Getting Started

This section guides you through the complete **Visual Layer** workflow for manufacturing defect detection, from dataset creation through model training. 

The following diagram outlines the recommended sequence for using **Visual Layer** within a standard defect-detection workflow.

        
        ![](images/vl-manufacturing-workflow-overview-diagram.png)
        
**The Primary Workflow**

        

The key steps of this workflow are as follows:

| **Step** | **Phase** | **Description** |
| --- | --- | --- |
| ![](images/1light.png) | **[Create & Prepare Dataset**](#how-dataset-creation-works) | Ingest your production imagery and metadata from manufacturing equipment into the **Visual Layer** platform, then explore it to prepare for label propagation. |
| ![](images/2light.png) | **[Label Propagation**](#how-label-propagation-works) | Add representative samples, automatically propagate labels to similar images, and review and validate labels to ensure consistency and accuracy across your dataset. |
| ![](images/3light.png) | **[Train Models Downstream**](#train-models-how-it-works) | Send your finalized, validated dataset to your model-training pipeline for deployment. |
