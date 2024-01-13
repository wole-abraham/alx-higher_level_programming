#!/usr/bin/python3
"""Base model"""


class Base():
    """Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes instance attributes"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
