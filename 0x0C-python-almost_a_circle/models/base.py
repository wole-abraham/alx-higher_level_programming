#!/usr/bin/python3
"""This base will be the base of all other classes in this project"""


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
