from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow import configuration as conf

from src.db_connection import *
from src.json_to_csv import *
from src.CSV_to_DB import *
from src.db_to_schema import *

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2024, 11, 1),
    'retries': 1, 
    'retry_delay': timedelta(minutes=0.5), 
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='Dag for data pipeline',
    schedule_interval=None,  
    catchup=False,
)

json_to_csv_review_data = PythonOperator(
    task_id='json_to_csv_review_data',
    python_callable=json_to_csv,
    op_args=['Data/Raw/TEST/test_user_reviews.json', 'Data/Raw_CSV/TEST/'],
    dag=dag,
)

json_to_csv_meta_data = PythonOperator(
    task_id='json_to_csv_meta_data',
    python_callable=json_to_csv,
    op_args=['Data/Raw/TEST/test_metadata.json','Data/Raw_CSV/TEST/'],
    dag=dag,
)



create_table_user_review = PythonOperator(
    task_id='create_table_user_review',
    python_callable=create_table_user_review,
    dag=dag,
)

create_table_meta_data = PythonOperator(
    task_id='create_table_meta_data',
    python_callable=create_table_meta_data,
    dag=dag,
)

add_meta_data = PythonOperator(
    task_id='add_meta_data',
    python_callable=add_meta_data,
    dag=dag,
)

add_user_reviews = PythonOperator(
    task_id='add_user_reviews',
    python_callable=add_user_reviews,
    dag=dag,
)

db_to_schema = PythonOperator(
    task_id='db_to_schema',
    python_callable=db_to_schema,
    dag=dag,
)








parallel_tasks_1 = [json_to_csv_review_data, json_to_csv_meta_data, create_table_user_review, create_table_meta_data]    
parallel_tasks_2 = [add_meta_data, add_user_reviews]

for task in parallel_tasks_1:
        task >> parallel_tasks_2

for task in parallel_tasks_2:
        task >> db_to_schema


# json_to_csv_review_data

if __name__ == "__main__":
    dag.cli()
