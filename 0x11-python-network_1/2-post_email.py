#!/usr/bin/python3
""" A script for POST request."""


if __name__ == "__main__":
    import sys
    from urllib import request, parse

    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
