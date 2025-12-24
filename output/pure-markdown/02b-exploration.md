# Create & Prepare: Explore {#exploration}

   **Visual Layer** automatically organizes your images into clusters during dataset creation. Each cluster groups visually similar images together and displays as a preview card showing:

   * **Number of items** - Total images in the cluster matching your current filters
   * **Representative thumbnails** - Key example images that summarize the cluster's visual patterns
   * **Prominent labels** - Most frequent labels within the cluster (if labels exist)

   ![Cluster preview cards](images/vl-clusters-image-view.png)

   Clusters help you quickly identify patterns and find similar defects without examining every image individually.
   
   Once your dataset is ready, spend time exploring it before beginning label propagation to identify representative examples for each defect class. This exploration phase is critical for selecting high-quality seed examples that will train the system effectively.

> **Tip:**  
> 
Spend sufficient time exploring before starting label propagation. The quality of your seed examples directly impacts automatic labeling accuracy. Look for clear, unambiguous examples that represent the full visual range of each defect class.

**Process:**

**To explore and prepare for label propagation**

1. From the **Dataset Inventory**, search or scroll to find your dataset and click its card to open it.

   The dataset loads in cluster view, displaying groups of visually similar images.

   Clusters help you quickly identify patterns and find similar defects without examining every image individually.

2. Look for clusters that clearly represent distinct defect types. Click any cluster to examine its images more closely and understand what visual patterns define each class.

3. Click ![](images/vl-filterbutton.png) to open the **Filter** options. For example, filter by **Folders** to examine images based on specific production runs.

   ![All Filters](images/vl-camtek-allfilters.png)

4. When you find a good example of a defect class, hover over the image and click ![](images/vl-visual-similarity-icon.png) to find similar images. This helps you locate all potential candidates for that class.

5. Based on your exploration, take note which defect classes are well-represented in your data and where you can find at least 5 clear, diverse examples for each class.

**Process:**

**Next Steps**

Now that you've explored your dataset and identified representative examples for each defect class, you're ready to begin [label propagation](#how-label-propagation-works).