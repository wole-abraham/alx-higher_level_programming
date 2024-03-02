#!/usr/bin/python3
# sends a post request

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    email = f'email={email}'.encode('utf-8')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as file:
        this = file.read()
        print(this.decode('utf-8'))
