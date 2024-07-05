#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as a:
        print(dict(a.headers).get("X-Request-Id"))
