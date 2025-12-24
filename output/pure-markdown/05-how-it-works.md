# Train Models: How It Works {#train-models-how-it-works}

Training models downstream is the last step in your primary **Visual Layer** workflow. You can train a model downstream when the dataset has achieved [**Train-Worthy** status](#progress-indicators-reference), allowing you to send the complete dataset downstream to train your Camtek models. This integrated training workflow eliminates manual data export and preparation steps.

**Visual Layer** automatically formats your labeled dataset and sends it to the Camtek training infrastructure with a single click. When sending the data for training, the system uses all labeled data from your completed label propagation, including seed examples, reviewed items, and high-confidence automatic labels. No manual data preparation is required. 

> **Note:**  
> 
You can use a single dataset to support the training of multiple models over time; however, you can only run one training session per dataset at a time.

The downstream model training process consists of the following substeps:

![](images/vl-train-models-diagram.png)

**Train Models Downstream Workflow**

| **Step** | **Phase** | **Description** |
| --- | --- | --- |
| ![](images/1light.png) | **Initiate Training** | Select your target Camtek model configuration and click **Train** to package and send your labeled dataset to the training infrastructure. |
| ![](images/2light.png) | **Monitor Progress** | Track training job status through the **Visual Layer** interface. View real-time updates as your model trains on the downstream infrastructure. |
| ![](images/3light.png) | **Review Results** | Access completed models in the Model Catalog to view training results, performance metrics, and deployment status. |
