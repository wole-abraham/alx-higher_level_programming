#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, encoding="utf-8", mode='w') as a_file:
        a_file.write(text)
    with open(filename, encoding="utf-8") as a_file:
        a_file.read()
        nb_char = a_file.tell()
    return nb_char
