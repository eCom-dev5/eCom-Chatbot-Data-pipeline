import os
import requests
import zipfile
import shutil
from src.bucket_connection import *




def ingest_data_meta(file_url):
    response = requests.get(file_url, timeout=30)
    filename = os.path.basename(file_url)
    zipfile_path = os.path.join('Data', 'temp1', filename)
    extract_to = os.path.join('Data', 'temp1')
    if response.status_code == 200:
        with open(zipfile_path, "wb") as file:
            file.write(response.content)
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

    extracted_files = []
    try:
        with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            extracted_files = zip_ref.namelist()  
    except zipfile.BadZipFile:
        print(f"Failed to unzip {zipfile_path}. It may not be a zip file.")
    nfile_name = str(extracted_files[0])
    temp_csv_file_path = os.path.join('Data', 'temp1', nfile_name)
    destination_blob_directory = "Data/Raw/TEST/"
    destination_blob_name = os.path.join(destination_blob_directory, nfile_name)
    upload_blob(temp_csv_file_path, destination_blob_name)
    folder_path='Data/temp1'
    shutil.rmtree(folder_path)
    os.makedirs(folder_path)
    message = "Done"
    return message



def ingest_data_review(file_url):
    response = requests.get(file_url, timeout=30)
    filename = os.path.basename(file_url)
    zipfile_path = os.path.join('Data', 'temp2', filename)
    extract_to = os.path.join('Data', 'temp2')
    if response.status_code == 200:
        with open(zipfile_path, "wb") as file:
            file.write(response.content)
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

    extracted_files = []
    try:
        with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            extracted_files = zip_ref.namelist()  
    except zipfile.BadZipFile:
        print(f"Failed to unzip {zipfile_path}. It may not be a zip file.")
    nfile_name = str(extracted_files[0])
    temp_csv_file_path = os.path.join('Data', 'temp2', nfile_name)
    destination_blob_directory = "Data/Raw/TEST/"
    destination_blob_name = os.path.join(destination_blob_directory, nfile_name)
    upload_blob(temp_csv_file_path, destination_blob_name)
    folder_path='Data/temp2'
    shutil.rmtree(folder_path)
    os.makedirs(folder_path)
    message = "Done"
    return message
    





    









 