#!/usr/bin/python3
"""This base will be the base of all other classes in this project"""

import json


class Base():
    """Base his base will be the base of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes instance attributes"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string represention
        for list of dictionaries
        """

        if list_dictionaries is None:
            return "[]"

        json_dic = json.dumps(list_dictionaries)
        return json_dic

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save the json str representation of list_obj to file

        """
        with open("Rectangle.json", mode='w', encoding="utf-8") as file:
            convert = cls.to_json_string(list_objs)
            file.write(json.dumps(convert))
