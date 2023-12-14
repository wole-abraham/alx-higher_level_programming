#!/usr/bin/python3
"""read a file to stdout
"""
def read_file(filename=""):
    """python script to open and read a file to stdout

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, encoding="utf-8", mode='r') as a_file:
        print(a_file.read())
