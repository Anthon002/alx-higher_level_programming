#!/usr/bin/python3
"""This script will list my 10 recent commits on a given GitHub repo.
"""
import sys
import requests as r


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    commits = r.get(url).json()
    limit = 10
    try:
        for j in range(limit):
            print("{}: {}".format(
                commits[j].get("sha"),
                commits[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
