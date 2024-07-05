#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    con = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(con.text)))
    print("\t- content: {}".format(con.text))
