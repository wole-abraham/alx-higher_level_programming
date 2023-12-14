#!/usr/bin/python3
"""writes a json representation of an object to file"""

import json


def save_to_json_file(my_obj, filename):
    """_summary_

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, encoding="utf-8", mode='w') as a_file:
        a_file.write(json.dumps(my_obj))
