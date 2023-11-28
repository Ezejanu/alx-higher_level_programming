#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        content = response.text.split()
        if content:
            print("{}".format(content[0]))

    except requests.exceptions.HTTPError as e:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
