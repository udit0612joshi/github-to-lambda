import requests
import lambda_function.lambda_handler


def test_api():
    res = requests.get('https://maas04yks8.execute-api.us-east-2.amazonaws.com/default/helloWorld')
    assert res.status_code == 200
    assert JSON_STRING == "helloWorld", "Output is not valid"
    assert res.json() == "helloworld", "Output is not valid"
