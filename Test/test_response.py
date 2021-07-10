import requests


def test_api():
    res = requests.get('https://maas04yks8.execute-api.us-east-2.amazonaws.com/default/helloWorld')
    output = res.status_code
    text = res.json()
    assert text == "helloworld", "Output is not valid"



