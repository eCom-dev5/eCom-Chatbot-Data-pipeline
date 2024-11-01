import os
from airflow import DAG
from datetime import datetime
from google.cloud import storage
from dotenv import load_dotenv
from sqlalchemy import text

from src.db_connection import *

load_dotenv()

def db_to_schema():
    postgres_conn_string = os.getenv("postgres_conn_string")
    engine = connect_with_db()
    with engine.begin() as connection:
        try:
            query = text("""CREATE TABLE IF NOT EXISTS productimages ( parent_asin TEXT, thumb TEXT, hi_res TEXT, large_res TEXT );  """)
            result = connection.execute(query)
            query = text("""CREATE TABLE IF NOT EXISTS productmetadata ( parent_asin TEXT, title TEXT, average_rating TEXT, rating_number TEXT, features TEXT, description TEXT, price TEXT, store TEXT, details TEXT, main_category TEXT );""")
            result = connection.execute(query)
            query = text("""CREATE TABLE IF NOT EXISTS productcategories ( parent_asin TEXT, categories TEXT );""")
            result = connection.execute(query)
            query = text("""CREATE TABLE IF NOT EXISTS userreviews ( rating TEXT, title TEXT, text TEXT, asin TEXT, parent_asin TEXT, user_id TEXT, timestamp TEXT, helpful_vote TEXT, verified_purchase TEXT );""")
            result = connection.execute(query)


            query = text("""DELETE FROM public.metadata m WHERE images NOT LIKE '%https://%';""")
            result = connection.execute(query)
            query = text("""UPDATE public.metadata SET images = REPLACE(images, '''', '"') WHERE images IS NOT NULL;""")
            result = connection.execute(query)
            query = text("""UPDATE public.metadata SET images = REPLACE(images, 'None', 'null') WHERE images IS NOT NULL;""")
            result = connection.execute(query)
            query = text("""INSERT INTO productimages (parent_asin, thumb, hi_res, large_res) SELECT parent_asin, COALESCE(images::jsonb -> 0 ->> 'thumb', '') AS thumb, COALESCE(images::jsonb -> 0 ->> 'hi_res', '') AS hi_res, COALESCE(images::jsonb -> 0 ->> 'large', '') AS large_res FROM public.metadata;""")
            result = connection.execute(query)

            query = text("""INSERT INTO productmetadata ( parent_asin, title, average_rating, rating_number, features, description, price, store, details, main_category ) SELECT parent_asin, title, average_rating, rating_number, features, description, price, store, details, main_category FROM public.metadata;""")
            result = connection.execute(query)
            query = text("""INSERT INTO productcategories ( parent_asin, categories ) SELECT parent_asin, categories FROM public.metadata;""")
            result = connection.execute(query)
            query = text("""INSERT INTO userreviews ( rating, title, text, asin, parent_asin, user_id, timestamp, helpful_vote, verified_purchase ) SELECT rating, title, text, asin, parent_asin, user_id, timestamp, helpful_vote, verified_purchase FROM public.user_reviews;""")
            result = connection.execute(query)

        except Exception as e:
            message = f"Error during insert: {e}"


