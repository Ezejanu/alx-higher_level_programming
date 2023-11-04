#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    response = requests.post(url, data=data)

    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)

    if response.status_code == 200 and response.text:
        try:
            data = response.json()
            if data:
                print("[{}] {}".format(data.get("id"), data.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print("No result")
