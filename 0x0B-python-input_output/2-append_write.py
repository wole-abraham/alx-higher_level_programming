#!/usr/bin/python3
"""append a string to file
"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, mode='a', encoding="utf-8") as a_file:
        a_file.write(text)
        nb_text = len(text)
    return nb_text
