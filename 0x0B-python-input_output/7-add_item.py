#!/usr/bin/python3
"""Summary"""
if __name__ == "__main__":

    import json
    import sys

    def save_to_json_file(my_obj, filename):
        """writes a json representation of an object to file

        Args:
            my_obj (_type_): _description_
            filename (_type_): _description_
        """
        with open(filename, encoding="utf-8", mode='w') as a_file:
            a_file.write(json.dumps(my_obj))

    def load_from_json_file(filename):
        """_summary_

        Args:
            filename (_type_): _description_
        """

        with open(filename, encoding="utf-8") as a_file:
            obj = json.loads(a_file.read())
        return obj
    i = 1
    list1 = []

    while i < len(sys.argv):
        list1.append(sys.argv[i])
        i += 1
    try:
        ab = load_from_json_file("add_item.json")
    except FileNotFoundError:
        save_to_json_file(list1, "add_item.json")
    else:
        for i in list1:
            ab.append(i)

        save_to_json_file(ab, "add_item.json")
