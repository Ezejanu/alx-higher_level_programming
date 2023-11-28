#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    response = requests.get(url)
    X_request_id = response.headers.get('X-Request-Id')
    if X_request_id:
        print("{}".format(X_request_id))
