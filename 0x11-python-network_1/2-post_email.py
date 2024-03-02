#!/usr/bin/python3
# sends a post request

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    email = f'email={sys.argv[2]}'
    data = email.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as file:
        this = file.read()
        print(this.decode('utf-8'))
