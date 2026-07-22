import io
import pandas as pd
from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator


BUCKET_NAME='sales-bucket2026'
GCS_BLOB_INPUT='raw/Sales_data_2026.csv'
GCS_BLOB_OUTPUT='cleaned/cleaned_sales_data.csv'
PROJECT_ID='project-3514b2e9-e0c7-4957-ad9'
DATASET='sales_analytics'
TABLE='Sales2026'


default_args={
    'owner':'Sales_ETL',
    'start_date':datetime(2026,7,13)
}

with DAG(
    dag_id='Sales_airflow',
    default_args=default_args,
    description='2026 Sales data ETL Pipeline',
    schedule=None,
    catchup=False
) as dag:
    

    def data_extraction(ti):

        gcs_hook=GCSHook(
            gcp_conn_id="google_cloud_default"
        )

        file_bytes=gcs_hook.download(

            bucket_name=BUCKET_NAME,

            object_name=GCS_BLOB_INPUT

        )

        df=pd.read_csv(io.BytesIO(file_bytes))

        return df.to_json()

    def data_transforming(ti):

        pulled_data=ti.xcom_pull(task_ids='extracted_data')

        df=pd.read_json(pulled_data)

    # cleaning data

        df['customer_name']=df['customer_name'].fillna('Unknown name')

        df['quantity']=df['quantity'].fillna(df['quantity'].median())

        df['region']= df['region'].fillna('Unknown place')
    # Removing duplicates

        df=df.drop_duplicates()
     
        df['order_date']=pd.to_datetime(df['order_date'],format='mixed',errors='coerce')

        df['order_date']=df['order_date'].dt.strftime('%Y-%m-%d')

    # Change the negative amount values into positive
        df['sales_amount']=df['sales_amount'].abs()

        df['discount_percent'] = df['discount_percent'].fillna(0)

    # Convert data types

        df['quantity']=df['quantity'].astype(int)

        df['unit_price']=df['unit_price'].astype(float)    

        df['sales_amount']=df['sales_amount'].astype(float)    


        return df.to_json()
    
    def loading_data(ti):
        pulled_data=ti.xcom_pull(task_ids='transformed_data')

        df=pd.read_json(pulled_data)

        csv_file=df.to_csv(index=False)

        gcs_hook=GCSHook(
            gcp_conn_id="google_cloud_default"
        )
        
        gcs_hook.upload(

            bucket_name=BUCKET_NAME,

            object_name=GCS_BLOB_OUTPUT,

            data=csv_file,
            
            mime_type='text/csv'
        )


    Task1=PythonOperator(

        task_id='extracted_data',

        python_callable=data_extraction
    )
    Task2=PythonOperator(

        task_id='transformed_data',

        python_callable=data_transforming
    )
    Task3=PythonOperator(

        task_id='loaded_data',

        python_callable=loading_data
    )
    
    load_to_bigquery=GCSToBigQueryOperator(

        task_id='load_to_bigquery',

        bucket=BUCKET_NAME,

        source_objects=[GCS_BLOB_OUTPUT],

        destination_project_dataset_table=f"{PROJECT_ID}.{DATASET}.{TABLE}",

        source_format='CSV',

        skip_leading_rows=1,

        autodetect=True,

        write_disposition='WRITE_TRUNCATE',

        gcp_conn_id='google_cloud_default',

    )


    Task1>>Task2>>Task3>>load_to_bigquery






