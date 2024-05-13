#!/usr/bin/python3

""" python script that display """

if __name__ == "__main__":

    import urllib.request
    
    import sys

    arg = sys.argv

    with urllib.request.urlopen(arg[1]) as file:
        print(file.headers.get('X-request-Id'))
