#!/usr/bin/python3
# gets response header value

"""Python to get x-request-id value from header file """

if __name__ == '__main__':
    import sys
    import urllib.request as urll

    with urll.urlopen(sys.argv[1]) as req:
        print(req.headers['X-Request-Id'])
