#!/usr/bin/python3
"""
A script that list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails” using the GitHub API

The script takes 2 arguments:

- Arg 1: Repository name
- Arg 2: Owner name
"""

import requests
import sys

if __name__ == "__main__":

    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"

    params = {
            "author": owner,
            "per_page": 10,
            }

    response = requests.get(url, params=params)

    commits = response.json()
    for commit in commits:
        sha = commit.get("sha")
        author_name = commit.get("commit", {}).get("author", {}).get("name",
                                                                     "Unkmowm")
        print(f"{sha}: {author_name}")
