#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as a:
        con = a.read()
        print("Body response:")
        print(f"    - type: {type(con)}")
        print(f"    - content: {con}")
        print(f"    - utf8 content: {con.decode('utf-8')}")
