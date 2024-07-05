#!/usr/bin/python3

"""
    python script that takes a url
    and an email, sends a Post

"""

from sys import argv
import urllib.request
import urllib.parse

if __name__ = "__main__":

    email = argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Reqest(argv[1], data)

    with urllib.request.urlopen(req) as file:
        print(file.read().decode('utf-8'))
