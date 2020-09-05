import config
import json
import requests

from logging_custom_message import logging_custom_message


def update_test_status(uin, test_status):
    test_status_code = None
    
    if test_status.lower() == "quarantine":
        test_status_code = "1"
    elif test_status.lower() == "isolate":
        test_status_code = "2"
    elif test_status.lower() == "release":
        test_status_code = "3"

    data = {
        "test_status": test_status_code 
    }
    
    endpoint = config.REDCAP_API_ENDPOINT + "/" + uin
    headers = {"Authorization": "xyz"}
    request = requests.put(endpoint, json=data, headers=headers)
    
    if request.status_code == 200:
        result = request.json()
        print(f'result:{result}')


if __name__ == "__main__":
    
    update_test_status(uin="333333333", test_status="isolate")
