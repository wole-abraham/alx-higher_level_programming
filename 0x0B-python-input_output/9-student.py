#!/usr/bin/python3
""" summary """


class Student():
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initializing arg"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ class tojson"""

        objs = vars(self)

        return objs
