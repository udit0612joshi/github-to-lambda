import requests
import lambda_function

def test_api():
    res = requests.get('https://maas04yks8.execute-api.us-east-2.amazonaws.com/default/helloWorld')
    output = res.status_code
    text = res.json()
    assert status_code == 200
    assert JSON_STRING=="helloWorld", "Output is not valid"
    assert text == "helloworld",  "Output is not valid"



