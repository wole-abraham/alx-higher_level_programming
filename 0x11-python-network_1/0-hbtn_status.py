#!/usr/bin/python3
#Python script fetches response from https://alx-intranet.hbtn.io/status
"""url fetcher"""

if __name__ == "__main__":
    import urllib as url
    with url.request.urlopen('https://alx-intranet.hbtn.io/status') as html:
        response = html.read()
        print(f'Body response:\n\t- type: {type(response)}\n\t- content: {response}\n\t- utf8 content: {response.decode("utf-8")}')
