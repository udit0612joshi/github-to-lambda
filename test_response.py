import requests
from lambda_function import *

def test_api():
    assert s3_read_write() == "helloworld" , "Output is not valid"
