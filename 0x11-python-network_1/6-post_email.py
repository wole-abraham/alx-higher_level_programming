#!/usr/bin/python3
# Python script sends a post reuqest within the url

""" Python script sends a post request within the url """

if __name__ == '__main__':
    import sys
    import requests
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    r = requests.post(url, email)
    print(r.text)
