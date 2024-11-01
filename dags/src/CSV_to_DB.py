import os
from airflow import DAG
from datetime import datetime
from google.cloud import storage
from dotenv import load_dotenv
from sqlalchemy import text

from src.db_connection import *
import time

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
    time.sleep(13)


def add_user_reviews():
    time.sleep(14)


# def csv_to_DB_user_review(bucket_name:str, file_name: str):
#     table_name = "user_reviews_test"
#     postgres_conn_string = os.getenv("postgres_conn_string")
#     instance_name = os.getenv("INSTANCE_CONNECTION_NAME")
#     database_name = os.getenv("DB_NAME")
    


#     transfer_command = f"""
#     gcloud sql import csv postgres gs://{bucket_name}/{file_name} \
#     --database={database_name} \
#     --table={table_name}
#     """
#     return transfer_command


# transfer_command = csv_to_DB_user_review('Data/Raw_CSV/TEST/','TEST.csv')
# print(transfer_command)
    

    





    













