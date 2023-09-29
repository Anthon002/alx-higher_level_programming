#!/usr/bin/python3
"""This script will send a request to the arg URL and display the body of the response
"""
from urllib import request as r
from urllib import error as e
import sys


if __name__ == "__main__":
    try:
        with r.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except e.HTTPError as err:
        print('Error code:', err.code)
