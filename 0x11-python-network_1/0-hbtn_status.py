#!/usr/bin/python3

"""
    python script that fetches http:/alx-intranet.hbtn.io/status
"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as file:
    res = file.read()

print(f'Body response:\n\t- type: {type(res)}\n\t- content: {res}\n\t- \
utf8 content: {res.decode()}')
