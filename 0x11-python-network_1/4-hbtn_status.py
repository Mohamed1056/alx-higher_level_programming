#!/usr/bin/python3
""" Script for fetching a URL."""


if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    s = r.text
    print("Body response:")
    print("\t- type: {}".format(type(s)))
    print("\t- content: {}".format(s))
