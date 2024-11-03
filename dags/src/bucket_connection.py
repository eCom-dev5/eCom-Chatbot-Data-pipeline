import os
from google.cloud import storage
from dotenv import load_dotenv

load_dotenv()

def connect_to_bucket():
    bucket_name = os.getenv("GCS_BUCKET_NAME")
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    return bucket

def upload_blob(source_file_name: str, destination_blob_name: str):
    bucket = connect_to_bucket()
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

def download_blob(source_blob_name: str, destination_file_name: str):
    bucket = connect_to_bucket()
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

def list_blobs():
    bucket = connect_to_bucket()
    blobs = bucket.list_blobs()
    print("Blobs in the bucket:")
    for blob in blobs:
        print(blob.name)


