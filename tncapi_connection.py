import requests

import config
from logging_custom_message import logging_custom_message


def lookup_name(uin):
    headers = {
        'x-api-key': config.TNC_API_KEY,
        'Accept': 'application/json'
    }

    result = requests.get(config.TNC_API_ENDPOINT + '/' + str(uin), headers=headers)
    if result.status_code == 200:
        logging_custom_message(result.json())
        return True, {"data": result.json()}
    elif result.status_code == 404:
        return False, {"message": result.json()["message"]}
    else:
        return False, {"message": "Cannot connect to Access Control API!"}


if __name__ == "__main__":
    print(lookup_name(uin="756561777"))
    print(lookup_name(uin="668905810"))