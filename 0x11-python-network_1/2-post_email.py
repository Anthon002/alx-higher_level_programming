#!/usr/bin/python3
"""
    This script will  take in a URL and an email,
    send a POST request to the passed URL with the email as a parameter, and displays the body of the response
"""
import urllib.request as ur
import urllib.parse as up
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = up.urlencode(value).encode("ascii")

    request = ur.Request(url, data)
    with ur.urlopen(request) as res:
        print(res.read().decode("utf-8"))
