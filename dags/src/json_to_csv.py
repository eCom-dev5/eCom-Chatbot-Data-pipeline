import os
import pandas as pd
from dotenv import load_dotenv
# from bucket_connection import upload_blob

from src.bucket_connection import *

load_dotenv()

def json_to_csv_meta(source_blob_name, destination_blob_directory):
    file_name = os.path.splitext(os.path.basename(source_blob_name))[0]
    temp_json_file_path = f'Data/temp/{file_name}.json'  
    temp_csv_file_path = f'Data/temp/{file_name}.csv'  
    download_blob(source_blob_name, temp_json_file_path)
    data = pd.read_json(temp_json_file_path)
    data.to_csv(temp_csv_file_path, index=False)
    destination_blob_name = os.path.join(destination_blob_directory, f'{file_name}.csv')
    upload_blob(temp_csv_file_path, destination_blob_name)
    os.remove(temp_json_file_path)
    os.remove(temp_csv_file_path)
    message = f'Successfully converted {source_blob_name} to CSV and uploaded to {destination_blob_name}'
    return message

def json_to_csv_review(source_blob_name, destination_blob_directory):
    file_name = os.path.splitext(os.path.basename(source_blob_name))[0]
    temp_json_file_path = f'Data/temp/{file_name}.json'  
    temp_csv_file_path = f'Data/temp/{file_name}.csv'  
    download_blob(source_blob_name, temp_json_file_path)
    data = pd.read_json(temp_json_file_path)
    data.to_csv(temp_csv_file_path, index=False)
    destination_blob_name = os.path.join(destination_blob_directory, f'{file_name}.csv')
    upload_blob(temp_csv_file_path, destination_blob_name)
    os.remove(temp_json_file_path)
    os.remove(temp_csv_file_path)
    message = f'Successfully converted {source_blob_name} to CSV and uploaded to {destination_blob_name}'
    return message







