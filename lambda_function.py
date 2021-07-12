import json
import boto3
from datetime import datetime

from boto3 import s3
from botocore.exceptions import ClientError

BUCKET_NAME = 'testbucket345346'
JSON_STRING = 'helloworld'
FILE_NAME = 'data.csv'


def s3_read_write():
    s3 = boto3.resource('s3')
    body = ""
    try:
        obj = s3.Object(BUCKET_NAME, FILE_NAME)
        body = obj.get()['Body'].read().decode()
    except ClientError:
        print("Key Not found")
    client = boto3.client('s3')
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    client.put_object(Body=str(body) + "\n" + date, Bucket=BUCKET_NAME, Key=FILE_NAME)
   

def hello_world():
    return json.dumps(JSON_STRING)

def lambda_handler(event, context):
    response = hello_world()
    s3_read_write()
    print(response)
    return {
        'statusCode': 200,
        'body': response
    }
