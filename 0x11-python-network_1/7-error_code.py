#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and display
# the body of the response.

""" Python script returns error code or url """

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.content.decode('utf-8'))
