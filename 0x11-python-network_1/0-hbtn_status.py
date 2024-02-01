#!/usr/bin/python3
""" Writing a script to fetch a URL."""


if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status/') as response:
        content = response.read()
        print("Body response:")
        print("\t- type:{}".format(type(content)))
        print("\t- content:{}".format(content))
        print("\t- utf8 content:{}".format(content.decode('utf-8')))
