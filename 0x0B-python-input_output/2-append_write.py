#!/usr/bin/python3
"""append a string to file
"""


def append_write(filename="", text=""):

    with open(filename, mode='a', encoding="utf-8") as a_file:
        a_file.write(text)
        nb_text = len(text)
    return nb_text

print(append_write("my_file.txt", "hey"))