#!/usr/bin/python3
# Python script that takes in a URL, returns the value of the header

"""
    python script

"""

import sys
import requests

url = sys.argv[1]
r = requests.get(url)
print(r.headers['X-Request-Id'])
