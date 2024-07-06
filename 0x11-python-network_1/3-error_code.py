#!/usr/bin/python3

"""
    python scritp that takes

"""

if __name__ == "__main__":

    from sys import argv
    import urllib.request
    import urllib.parse

    url = argv[1]

    try:
        with urllib.request.urlopen(url) as file:
            res = file

    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
    else:
        print(res.read().decode())
