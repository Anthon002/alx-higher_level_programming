#!/usr/bin/python3
"""
This script witll fetch https://intranet.hbtn.io/status.
"""
import requests as r


if __name__ == "__main__":
    request = r.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
