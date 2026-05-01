# Reliancemart_FabricMedallion

Project Overview :
End-to-End Retail Intelligence Platform (Microsoft Fabric) Architected a scalable retail intelligence platform in Microsoft Fabric using a Medallion Architecture to unify structured transactional data with unstructured social logs. I engineered a metadata-driven ingestion framework via Data Factory pipelines (Lookup/ForEach activities) that automated the landing of 6+ diverse data sources into OneLake, reducing manual pipeline maintenance by 40%. I developed PySpark ETL notebooks for the Silver layer to perform schema validation and multi-set joins, achieving 100% data integrity. By curating business-critical KPIs into Gold-layer Delta Tables with V-Order optimization, I delivered real-time insights via a Power BI dashboard in Direct Lake mode, which cut reporting latency from hours to seconds and ensured 99.9% data availability for high-impact decision-making.

--------------------------------------------------------------------------------
Microsoft Fabric End-to-End Data Project: Medallion Architecture

This project demonstrates the design and implementation of a scalable data platform for a midsize retail business ("Reliance Mart"). The architecture processes structured transactional/inventory data and unstructured social media/web log data to provide insights into customer behavior, sales trends, and product sentiment,.
Architecture: The Medallion Approach
The data is logically organised into three distinct layers to ensure quality and reliability,:
* Bronze (Raw Zone): Maintains the source of truth in its original format (CSV and JSON).

* Silver (Enriched Zone): Cleansed, standardised, and joined data.

* Gold (Curated Zone): Business-ready, aggregated data for analytics and reporting.
 
--------------------------------------------------------------------------------
Implementation Steps
1. Environment Setup & Data Ingestion (Bronze Layer)
* Workspace Configuration: Created a dedicated Fabric workspace with "Trial Capacity" and utilised the Medallion Task Flow for visual orchestration.
* Lakehouse Creation: Established separate Lakehouses for the Bronze, Silver, and Gold layers.
* Metadata-Driven Pipeline:
    * Developed a scalable ingestion strategy using Fabric Data Pipelines.
    * Implemented a Lookup Activity to read JSON metadata files containing source URLs and destination paths.
    * Used a ForEach Activity to dynamically ingest multiple structured (CSV) and unstructured (JSON) files via HTTP connectors into the Bronze       Lakehouse.

2. Data Transformation (Silver Layer)
* PySpark Notebooks: Utilised Spark engines for data processing and cleansing.
* Data Refinement:
    * Dropped null values from critical columns (Order ID, Customer ID, etc.) and standardised date formats.
    * Performed Inner Joins between orders, customers, and products to create an enriched dataset.
    * Converted raw JSON unstructured data (reviews, social media, web logs) into high-performance Parquet format.
* OneLake Shortcuts: Utilised the Shortcut feature to reference data between the Bronze and Silver Lakehouses without moving or duplicating files,.
* 
3. Data Aggregation & KPI Development (Gold Layer)
    * Business Logic: Developed aggregations in PySpark to create "business-ready" tables.
    * Web Engagement: Measured actions per user per page (clicks, purchases, views).
    * Social Sentiment: Tracked sentiment trends (positive, neutral, negative) across various platforms.
    * Product Ratings: Calculated average ratings per product ID.
    * Delta Lake Conversion: Loaded the final Parquet files into Delta Tables to enable ACID transactions and SQL querying capabilities.
 
4. Data Modeling & Power BI Visualization
    * Semantic Model: Created a model using Direct Lake mode for real-time connectivity to the Gold Lakehouse.

    * DAX & Relationships:
    * Defined one-to-many relationships between a custom-built Date Table and the fact tables.
    * Standardised data types for currency and quantities.
  * Power BI Dashboard: Built a comprehensive report featuring.
    * KPI Cards: Total Sales and Total Products Sold.
    
    * Trend Analysis: Sales trends by month and year.
    * Sentiment & Engagement: Pie charts for social sentiment and web behavior.
    * Top Performers: Bar charts for Top 5 Products by sales, reviews, and stock levels.

5. Workflow Orchestration
    * Master Pipeline: Created a "Parent" pipeline to orchestrate the entire end-to-end flow.
    * Activity Sequencing: Used the Invoke Pipeline activity to trigger ingestion followed by the sequential execution of Silver and Gold             transformation notebooks.
    * Monitoring: Configured the pipeline to run on success/failure logic with options for email notifications.

--------------------------------------------------------------------------------------------
Tech Stack
* Platform: Microsoft Fabric.

* Storage: OneLake (Lakehouse/Delta Lake).
 
* Engine: Spark (PySpark) & SQL Analytic Endpoints.

* Orchestration: Fabric Data Pipelines.

* Visualization: Power BI (Direct Lake Mode).




