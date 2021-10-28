#!/usr/bin/env python

import requests
import json


def get_current_ip():
    """To get the current IP, use the API at
    https://api.ipify.org/?format=json"""

    url_api = "https://api.ipify.org/?format=json"

    try:
        requests_data = requests.get(url=url_api)
    except:
        return "Website did not send anything back that was usable"
    if requests_data.status_code != 200:
        return "API did not send anything back that was usable"
    else:
        current_ip = json.loads(requests_data.text)["ip"]

    return current_ip


if __name__ == "__main__":
    my_ip = get_current_ip()
    print(my_ip)
