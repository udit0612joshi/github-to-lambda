import json
import boto3
from datetime import datetime

from boto3 import s3
from botocore.exceptions import ClientError

BUCKET_NAME = 'testbucket345346'
JSON_STRING = 'byteworld'
FILE_NAME = 'data.csv'


def respond(res):
    return {
        'statusCode': '200',
        'body': json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


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


def lambda_handler(event, context):
    s3_read_write()
    return {
        'statusCode': 200,
        'body': json.dumps(JSON_STRING)
    }
