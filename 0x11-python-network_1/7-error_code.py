#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    a = requests.get(url)
    if (a < 400):
        print(a.text)
    print('Error code:', a.status_code)
