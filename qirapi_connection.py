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
    
    if config.QIR_API_ENDPOINT.endswith('/'):
        endpoint = config.QIR_API_ENDPOINT + uin
    else:
        endpoint = config.QIR_API_ENDPOINT + '/' + uin

    headers = {"Authorization": config.QIR_API_KEY}
    try:
        request = requests.put(endpoint, json=data, headers=headers)
    except Exception as ex:
        return False, {"message": str(ex)}
 
    if request.status_code == 200:
        logging_custom_message({"data": "Successfully updated the new status to QIR"})
        return True, {"data": "Successfully updated the new test status to QIR"}
    else:
        return False, {"message":"Cannot update the new test status to QIR"}


if __name__ == "__main__":
    print(update_test_status(uin="664937428", test_status="isolate"))
