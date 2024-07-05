#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import sys
import requests

if __name__ == "__main__":
    a = requests.get(sys.argv[1])
    print(dict(a.headers).get("X-Request-Id"))
