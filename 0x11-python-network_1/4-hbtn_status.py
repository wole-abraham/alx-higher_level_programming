#!/usr/bin/python3
# Python script that fetches are request

""" Python script tsht fetches a request  """

import requests

url = 'https://alx-intranet.hbtn.io/status'
r = requests.get(url)
print(f"Body response:\n\t- type: {type(r.text)}\n\t- content: {r.text}")
