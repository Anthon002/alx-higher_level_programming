#!/usr/bin/python3
"""This script will display the X-Request-Id header var of a request to arg  URL
"""
import sys
import requests as r


if __name__ == "__main__":
    url = sys.argv[1]
    
    print(r.get(url).headers.get("X-Request-Id"))
