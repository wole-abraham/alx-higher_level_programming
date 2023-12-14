#!/usr/bin/python3


"""read a file to stdout
"""
def read_file(filename=""):
    """python script to open and read a file to stdout

    Args:
        filename (str, optional): _description_. Defaults to "".
    """

    with open(filename, encoding="utf-8") as a_file:
        print("{}".format(a_file.read().rstrip()))
