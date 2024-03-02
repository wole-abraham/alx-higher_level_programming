#!/usr/bin/python3
# Python scripts takes a url and displays the decoded reesponse in utf-8

""" Python script to display the decode response of a url in utf-8"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as file:
            data = file.read().decode('utf-8')
            print(data)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
