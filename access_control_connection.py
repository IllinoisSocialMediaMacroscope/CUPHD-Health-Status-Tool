import requests

import config
from logging_custom_message import logging_custom_message


def lookup_access_status(uin):
    headers = {
        'x-api-key': config.ACCESSCTRL_KEY,
        'Accept': 'application/json'
    }

    result = requests.get(config.ACCESSCTRL_API_ENDPOINT + '/' + str(uin), headers=headers)
    if result.status_code == 200:
        logging_custom_message(result.json())
        return True, {"data": result.json()}
    elif result.status_code == 404:
        return False, {"message": result.json()["message"]}
    else:
        return False, {"message": "Cannot connect to Access Control API!"}

def update_access_status(uin, allowAccess: bool):
    """

    :param uin:
    :param allowAccess: "true" or "false"
    :return:
    """
    headers = {
        'x-api-key': config.ACCESSCTRL_KEY,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {
        "uin": uin,
        "allowAccess": allowAccess
    }
    result = requests.put(config.ACCESSCTRL_API_ENDPOINT, headers=headers, json=data)

    if result.status_code == 200:
        logging_custom_message(result.json())
        return True, {"data": result.json()}
    elif result.status_code == 404:
        return False, {"message": result.json()['message']}
    else:
        return False, {"message": "Cannot connect to Access Control API!"}


if __name__ == "__main__":
    print(lookup_access_status(uin="123"))
    print(lookup_access_status(uin="668905810"))
    print(update_access_status(uin="123", allowAccess=False))
    print(update_access_status(uin="668905810", allowAccess=False))