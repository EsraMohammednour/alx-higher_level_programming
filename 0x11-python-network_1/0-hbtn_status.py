#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as a:
        con = a.read()
        print("Body response:")
        print(f"\t - type: {type(con)}")
        print(f"\t - content: {con}")
        print(f"\t - utf8 content: {con.decode('utf-8')}")
