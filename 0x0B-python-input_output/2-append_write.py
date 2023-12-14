#!/usr/bin/python3
"""append a string to file
"""
import io


def append_write(filename="", text=""):

    with open(filename, mode='a', encoding="utf-8") as a_file:
        a_file.write(text)
        a = io.StringIO(text)
        a.read()
        nb_text = a.tell()
    return nb_text
