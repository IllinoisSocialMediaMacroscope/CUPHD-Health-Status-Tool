import config
import json
import requests

from logging_custom_message import logging_custom_message


def update_test_status(uin, test_status):
    test_status_dict = {
        "quarantine": "1",
        "isolate": "2",
        "release": "3",
    }
   
    data = {}
    try:
        data = {
            "test_status": test_status_dict[test_status] 
        }
    except KeyError as ke:
        print(f"Test status, {test_status} doesn't exist")
        return
    
    endpoint = config.REDCAP_API_ENDPOINT + "/" + uin
    headers = {"Authorization": "xyz"}
    request = requests.put(endpoint, json=data, headers=headers)
    
    if request.status_code == 200:
        result = request.json()
        print(f'result:{result}')
    else:
        print(f"Request failed with status_code: {request.status_code}")

if __name__ == "__main__":
    update_test_status(uin="333333333", test_status="isolate1")
