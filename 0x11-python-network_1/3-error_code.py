#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    r = Request(url)
    try:
        with urlopen(r) as a:
            print(dict(a.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: ",e.code)
