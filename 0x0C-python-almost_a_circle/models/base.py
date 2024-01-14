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
        with open(f"{cls.__name__}.json", mode='w', encoding="utf-8") as file:
            if list_objs is None:
                file.write(json.dumps([]))
            else:
                objs_dic = [x.to_dictionary() for x in list_objs]
                objs_dic = cls.to_json_string(objs_dic)
                file.write(objs_dic)

    def from_json_string(json_string):
        """
         Returns the list of the json string
         representation
        """

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates an instance withh all attr from **kwargs
        and returns the instance
        """
        if "size" in dictionary.keys():
            dummy = cls(1)
        else:
            dummy = cls(5, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            a = open(f"{cls.__name__}.json")
            file_content = a.read()
            loads = cls.from_json_string(file_content)
            list_int = [cls.create(**i) for i in loads]
            a.close()
        except FileNotFoundError:
            list_int = []

        return list_int
