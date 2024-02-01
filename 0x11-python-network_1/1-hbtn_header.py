#!/usr/bin/python3
""" Writing a script for reading the
header of the response ."""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as res:
        con = res.info()
        print(con.get('X-Request-Id'))
