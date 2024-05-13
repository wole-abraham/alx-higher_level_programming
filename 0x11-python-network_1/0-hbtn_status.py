#!/usr/bin/python3

""" python script fetches contenr from sitw"""

if __name__ == "__main__":

    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as file:
        re = file.read()

    print(f"Body response:\n\t- type: {type(re)}\n\t- content: {re}\
\n\t- utf8 content: {re.decode()}")
