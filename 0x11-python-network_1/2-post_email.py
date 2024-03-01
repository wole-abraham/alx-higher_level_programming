#!/usr/bin/python3
# sends a post request

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as file:
        print(file.read())






