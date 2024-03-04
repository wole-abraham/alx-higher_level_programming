#!/usr/bin/python3
# Python script

""" Python script """

if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        query = {'q': sys.argv[1]}
        r = requests.post(url, query)
        if isinstance(r.json(), dict) and len(r.json()) != 0:
            dic = r.json()
            print(f"[{dic['id']}] {dic['name']}")
        else:
            print("No result")
    else:
        print("No result")
