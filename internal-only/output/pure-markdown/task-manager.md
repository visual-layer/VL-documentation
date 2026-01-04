# Task Manager {#task-manager}

The **Task Manager** provides a unified view of all dataset-related operations across your **Visual Layer** workspace. It tracks processes such as dataset creation<!--media addition,  -->, label propagation, and model training, displaying their current status, progress, and any errors that occurred.

Use the **Task Manager** to:

* Monitor active operations in real-time
* Track operation history from the past 14 days
* Identify and troubleshoot failed processes

> **Note:**  
> 
The **Task Manager** maintains a visible history of all operations performed in the past 14 days. 

The **Task Manager** displays near real-time updates on all operations.

To access the **Task Manager**:

1. Go to the **Navigation Panel** on the left side of the screen.

2. Click ![Task Manager icon](images/vl-task-manager-icon.png).

   The **Task Manager** opens, displaying all operations from the past 14 days, similar to the following: 

   ![](images/vl-task-manager.png)

> **Note:**  
> 
If no operations have been performed in the past 14 days, the table appears empty with a notification indicating no recent activity.

The **Task Manager** displays all operations in a comprehensive table. Each row represents a single task and contains the following information:

| **Column** | **Description** |
| --- | --- |
| **Dataset Name** | The name of the dataset where the operation is running or was performed. Click the dataset name to navigate directly to its Explore page. |
| **Dataset ID** | The unique identifier for the dataset. Use filters to search by specific dataset IDs. |
| **Job** | The job identifier from your manufacturing equipment metadata. Each dataset contains a single job value. Use the filter to view tasks by specific jobs. |
| **Setup** | The setup identifier from your manufacturing equipment metadata. Each dataset contains a single setup value. Use the filter to view tasks by specific setups. |
| **Recipe** | The recipe identifier(s) from your manufacturing equipment metadata. A dataset may contain multiple recipe values. If the recipe name exceeds the cell width, it appears truncated with "..." — hover over the cell to view all recipe values. Use the filter to view tasks by specific recipes. |
| **Task** | The type of operation being performed: **Dataset Creation**<!-- **Media Addition**, --> **Label Propagation**, **Training Model**, or **Re-indexing**. Use the filter to view specific task types. |
| **Start Time** | The timestamp when the operation was initiated. Use the filter to view tasks from the last 24 hours, last 7 days, or last 14 days. |
| **Duration** | The elapsed time since the operation started (for running tasks) or the total time the operation took (for completed tasks). Sort by this column to identify long-running operations. |
| **Status** | The current state of the operation. See the Status Types section below for detailed descriptions of each status. Use the filter to view tasks with specific statuses. |
| **Actions** | Retrieve Task ID. |

> **Note:**  
> 
The **Task Manager** tracks operation-level status independently from overall dataset status. A dataset can show **Ready** status in the **Dataset Inventory** even when the **Task Manager** displays completed tasks  like **Training** <!-- or **Media Addition**,  -->since these operations do not block dataset access.

## Status Types {#task-statuses}

All tasks display one of several statuses to indicate their current state. Each status includes a percentage to show progress through the operation.

> **Note:**  
> 
See [Task Manager Status Types](#task-manager-statuses) in the **Appendices** for detailed descriptions of all task statuses and their meanings.

## Working with the Task Manager Table

The table displays tasks ordered by **Start Time** by default, with the most recent operations appearing first. Each column in the **Task Manager** supports filtering, grouping and sorting to help you quickly locate specific operations:

* **Filtering**: Click the filter icon in any column header, select the desired values, and click **Apply** to update the table.
* **Sorting**: Click the column header to sort tasks in ascending or descending order.