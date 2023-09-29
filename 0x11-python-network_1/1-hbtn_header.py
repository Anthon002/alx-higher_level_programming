#!/usr/bin/python3
"""
    this script takes a url and sends a request to display the value of X-request-Id var
"""
import urllib.request as ur
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    requesting = ur.Request(url)
    with ur.urlopen(requesting) as respond:
        print(dict(respond.headers).get("X-Request-Id"))
