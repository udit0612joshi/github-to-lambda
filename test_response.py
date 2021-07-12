import requests
from lambda_function import *

def test_api():
    print(s3_read_write())
    assert s3_read_write() == "helloworld" , "Output is not valid"
