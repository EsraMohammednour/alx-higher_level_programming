#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request

if __name__ == "__main__":
     u = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(u) as a:
        con = a.read()
        print("Body response:")
        print(f"\t - type: {type(con)}")
        print(f"\t - content: {con}")
        print(f"\t - utf8 content: {con.decode('utf-8')}")
