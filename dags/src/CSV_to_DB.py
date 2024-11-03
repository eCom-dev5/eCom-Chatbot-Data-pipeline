import os
from airflow import DAG
from datetime import datetime
from google.cloud import storage
from dotenv import load_dotenv
from sqlalchemy import text
import subprocess

from src.db_connection import *


load_dotenv()

def create_table_user_review():
    postgres_conn_string = os.getenv("postgres_conn_string")
    engine = connect_with_db()
    with engine.begin() as connection:
        try:
            query = text("""CREATE TABLE IF NOT EXISTS user_reviews ( rating TEXT, title TEXT, text TEXT, images TEXT, asin TEXT, parent_asin TEXT, user_id TEXT, timestamp TEXT, helpful_vote TEXT, verified_purchase TEXT ); """)
            result = connection.execute(query)
        except Exception as e:
            message = f"Error during insert: {e}"



def create_table_meta_data():
    postgres_conn_string = os.getenv("postgres_conn_string")
    engine = connect_with_db()
    with engine.begin() as connection:
        try:
            query = text("""CREATE TABLE IF NOT EXISTS metadata ( main_category TEXT, title TEXT, average_rating TEXT, rating_number TEXT, features TEXT, description TEXT, price TEXT, images TEXT, videos TEXT, store TEXT, categories TEXT, details TEXT, parent_asin TEXT, bought_together TEXT, subtitle TEXT, author TEXT );  """)
            result = connection.execute(query)
        except Exception as e:
            message = f"Error during insert: {e}"



def add_meta_data():
    bucket_name = "mlops_data_pipeline/Data/Raw_CSV/TEST"
    file_name = 'test_metadata.csv'
    postgres_conn_string = os.getenv("postgres_conn_string")
    table_name = 'metadata'
    transfer_command = f"""
    yes | gcloud sql import csv data-wharehousing \
    gs://{bucket_name}/{file_name} \
    --project=dockdecoder \
    --database=postgres \
    --table={table_name}
    """

    try:
        # Run the command
        result = subprocess.run(transfer_command, shell=True, check=True, capture_output=True, text=True)
        print("Import successful:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error during import:", e.stderr)


def add_review_data():
    bucket_name = "mlops_data_pipeline/Data/Raw_CSV/TEST"
    file_name = 'test_user_reviews.csv'
    postgres_conn_string = os.getenv("postgres_conn_string")
    table_name = 'user_reviews'
    transfer_command = f"""
    yes | gcloud sql import csv data-wharehousing \
    gs://{bucket_name}/{file_name} \
    --project=dockdecoder \
    --database=postgres \
    --table={table_name}
    """

    try:
        # Run the command
        result = subprocess.run(transfer_command, shell=True, check=True, capture_output=True, text=True)
        print("Import successful:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error during import:", e.stderr)













