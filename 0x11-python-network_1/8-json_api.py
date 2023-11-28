#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":

    #    q = sys.argv[1] if len(sys.argv) > 1 else ""
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if all(65 <= ord(char) <= 90 or 97 <= ord(char) <= 122
                for char in arg):
            q = arg
        else:
            q = ""
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    response = requests.post(url, data=data)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
