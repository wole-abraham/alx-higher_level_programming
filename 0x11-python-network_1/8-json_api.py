#!/usr/bin/python3
# Python script

""" Python script """

if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        query = {'q': sys.argv[1]}
    elif len(sys.argv) == 1:
        query = {'q': ""}
    r = requests.post(url, query)
    if isinstance(r.json(), dict) and len(r.json()) != 0:
        dic = r.json()
        print(f"[{dic['id']}] {dic['name']}")
    elif not isinstance(r.json(), list) and not isinstance(r.json(), tuple):
        print("Not a valid JSON")
    elif not isinstance(r.json(), dict):
        print("Not a valid JSON")
    else:
        print("No result")
