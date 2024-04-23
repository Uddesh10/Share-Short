import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv
load_dotenv()

def uploadImage(file , file_name):
    s3_client = boto3.client('s3')
    try:
        fileName = file_name+'.'+file.name.split('.')[1]
        response = s3_client.upload_fileobj(file, os.getenv('s3bucketname'), fileName)
    except ClientError as e:
        return ''
    return fileName