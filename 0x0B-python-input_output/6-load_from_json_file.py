#!/usr/bin/python3
"""Creates an object from a Json file"""
import json


def load_from_json_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_
    """

    with open(filename, encoding="utf-8") as a_file:
        obj = json.loads(a_file.read())

    return obj
