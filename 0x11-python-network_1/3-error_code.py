#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            output = content.split()
            if output:
                print(output[0])

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
