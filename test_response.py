import requests
from lambda_function import *

def test_api():
    res = requests.get('https://maas04yks8.execute-api.us-east-2.amazonaws.com/default/helloWorld')
    assert JSON_STRING == "helloworld", "Output is not valid"
    assert res.json() == "helloworld", "Output is not valid"
