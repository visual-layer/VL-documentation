# Integrating **Visual Layer** in Manufacturing Workflows
**Visual Layer** is a unified platform, designed to help teams manage, curate, and analyze visual data at scale, streamlining the entire data lifecycle. The platform provides centralized tools for exploring datasets, identifying patterns, maintaining data quality, and collaborating across teams.

> **Tip:**  
> 
**New to Visual Layer terminology?** A comprehensive glossary with detailed definitions, examples, and context for all concepts can be found in the [Key Concepts](#key-concepts) section of the Appendices.

Key capabilities for Camtek users include:

* Automated human-in-the-loop labeling
* Performance analysis and tracking
* Integration with the Camtek training infrastructure for real-time model deployment

The rest of this section describes:

* [Key concepts](#key-concepts)
* [Prerequisites for exploring datasets with Visual Layer](#browser-requirements)

## Key Concepts

Before exploring **Visual Layer**, familiarize yourself with these core concepts:

| **Concept** | **Description** |
| :---- | :---- |
| **Class** | Each distinct type of label in your classification system. You need at least two classes, each with enough examples. |
| **Class Taxonomy** | The complete structure of all possible classes defined in classes.json from your AOI machine output. Cannot be changed after dataset creation. |
| **Cluster** | A group of visually similar images automatically organized by **Visual Layer** |
| **Confidence Score** | A numerical measure (0-100%) indicating how certain the system is about an automatically assigned label. |
| **Dataset** | A collection of images and associated metadata organized for analysis and labeling |
| **Embedding** | The technology that enables **Visual Layer** to find visually similar images and automatically label thousands from just a few examples. |
| **Ground Truth** | Verified, accurate labels serving as the authoritative reference for training and evaluating machine learning models. |
| **Label** | The category assigned to a single image—the answer to "what type is this?" |
| **Label Propagation** | Semi-supervised learning combining automated pattern recognition with human oversight to efficiently label large datasets. |
| **Seed** | Initial labeled examples provided for each class. These training examples teach the system what each class looks like. |

> **Tip:**  
> 
**Need more detail?** For comprehensive definitions with examples and usage context, see the [Key Concepts](#key-concepts) section in the **Appendices**.

## Prerequisites {#browser-requirements}

Chrome browser required.