import requests
from lambda_function import *

def test_api():
    hello_world() == "helloworld" , "Output is not valid"
