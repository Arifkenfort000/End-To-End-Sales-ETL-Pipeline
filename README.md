End-to-End Sales ETL Pipeline using Google Cloud, Apache Airflow & Power BI
Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline for processing sales data using Google Cloud Platform. Raw sales data is stored in Google Cloud Storage, transformed using Python (Pandas) within an Apache Airflow workflow, loaded into BigQuery, and finally visualized in Power BI to generate business insights.

Architecture
Raw Sales CSV
       │
       ▼
Google Cloud Storage
       │
       ▼
Apache Airflow
       │
       ▼
Python (Pandas)
       │
       ▼
Cleaned CSV
       │
       ▼
BigQuery
       │
       ▼
Power BI Dashboard
Business Problem

Companies often receive sales data containing:

Missing values
Duplicate records
Incorrect date formats
Negative values
Blank fields

These quality issues make the data unsuitable for direct analytics. The goal of this project is to automate cleaning, store the processed data in BigQuery, and visualize insights in Power BI.

Dataset
Sales Transactions
520 Records
10 Columns
CSV Format

The dataset intentionally contains common data quality issues to simulate a real-world ETL scenario.

Technologies Used
Google Cloud Storage
Apache Airflow
Python
Pandas
BigQuery
Power BI
ETL Workflow
Extract

Read the raw CSV file from Google Cloud Storage.

Transform
Remove duplicate records
Handle missing values
Standardize dates
Correct negative values
Convert data types
Load
Upload cleaned CSV to Cloud Storage
Load into BigQuery
Visualization

Create an interactive Power BI dashboard connected to BigQuery.

Dashboard Highlights

The Power BI dashboard reports:

Total Revenue: 25.72M
Total Orders: 520
Total Quantity: 3K
Average Order Value: 50.92K
Average Discount: 8.37%
Highest revenue product: Laptop
Top customer: Jack
Highest sales region: North
Skills Demonstrated
ETL Pipeline Design
Data Cleaning
Apache Airflow
Google Cloud Storage
BigQuery
Python (Pandas)
SQL
Power BI
Data Engineering