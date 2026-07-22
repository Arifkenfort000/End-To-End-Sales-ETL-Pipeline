# 🚀 End-to-End Sales ETL Pipeline using Google Cloud, Apache Airflow & Power BI

## 📖 Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for processing sales data using Google Cloud Platform. The pipeline automates data ingestion, cleaning, transformation, storage, and visualization to convert raw sales data into meaningful business insights. Raw sales data is stored in Google Cloud Storage, transformed using Python (Pandas) within an Apache Airflow workflow, loaded into BigQuery, and visualized in Power BI for interactive reporting.

# 🎯 Project Objectives
Build an automated ETL pipeline for sales data.
Clean and transform raw datasets using Python (Pandas).
Orchestrate the workflow using Apache Airflow.
Store processed data in Google BigQuery.
Create interactive dashboards in Power BI for business analysis.

## 🏗️ Architecture

Raw Sales CSV
        │
        ▼
Google Cloud Storage
        │
        ▼
Apache Airflow (Cloud Composer)
        │
        ▼
Python (Pandas)
(Data Cleaning & Transformation)
        │
        ▼
Cleaned CSV
        │
        ▼
Google BigQuery
        │
        ▼
Power BI Dashboard


## 🛠️ Tech Stack
Google Cloud Storage
Apache Airflow (Cloud Composer)
Python
Pandas
Google BigQuery
Power BI
SQL


## 📂 Dataset

The project uses a sales transaction dataset containing 520 records and 10 columns. To simulate real-world business scenarios, the dataset intentionally includes missing values, duplicate records, inconsistent date formats, and negative values that are cleaned during the ETL process.

## ⚙️ ETL Workflow

### 1️⃣ Extract
Read raw sales data from Google Cloud Storage.
Load the data into a Pandas DataFrame.

### 2️⃣ Transform
Handle missing values.
Remove duplicate records.
Standardize date formats.
Correct invalid values.
Convert data types.

### 3️⃣ Load
Upload the cleaned dataset back to Cloud Storage.
Load the processed data into Google BigQuery.

### 4️⃣ Visualize
Connect Power BI to BigQuery.
Build interactive dashboards for business insights.

## 📊 Dashboard Insights

The Power BI dashboard provides key business metrics, including:

Total Revenue
Total Orders
Total Quantity Sold
Average Order Value
Average Discount
Top Revenue-Generating Products
Top Customers
Regional Sales Performance
Monthly Sales Trends
Interactive Filters for Region, Category, and Quarter

### 💡 Skills Demonstrated
ETL Pipeline Development
Data Cleaning & Transformation
Workflow Orchestration with Apache Airflow
Cloud Data Engineering
BigQuery Data Warehousing
SQL for Analytics
Power BI Dashboard Development
Python (Pandas)
📸 Project Screenshots
Project Architecture
Google Cloud Storage Buckets
Airflow DAG
DAG Execution
BigQuery Tables
Power BI Dashboard
🚀 Future Enhancements
Schedule automatic pipeline execution.
Add data quality validation checks.
Implement monitoring and alerting.
Support incremental data loading.
Integrate CI/CD for deployment.

### 👨‍💻 Author

Muhammed Arifudheen T
