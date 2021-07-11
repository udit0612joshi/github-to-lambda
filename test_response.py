import requests
from lambda_function import *

def test_api():
    res = requests.get('https://maas04yks8.execute-api.us-east-2.amazonaws.com/default/helloWorld')
    assert JSON_STRING == "helloWorld", "Output is not valid"
