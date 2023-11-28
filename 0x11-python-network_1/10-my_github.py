#!/usr/bin/python3
"""
A script that takes my GitHub credentials (username and password)
and uses the GitHub API to display your id

Basic Authentication with a personal access token as password to
access the information is needed

The script takes two(2) arguments:
- The first argument is the username
- The second argument is the password
(in this case, a personal access token as password)
"""

import requests
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    PAT = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, PAT))

    user_data = response.json()
    user_id = user_data.get("id")
    if user_id:
        print(user_id)
    else:
        print("None")
