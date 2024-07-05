#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as a:
            print(a.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
