#!/usr/bin/python3

"""
    python script takes a url
    sends a get request and
    displays the X-Request-Id
    variable foun din the header of the response

"""

import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
