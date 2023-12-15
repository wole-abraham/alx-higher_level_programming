#!/usr/bin/python3
"""sumary"""


class Student():
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initializing arg"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ class tojson"""
        attrib = vars(self)

        if attrs is None:
            return attrib
        else:
            filtered_dic = {key: attrib[key] for key in attrib if key in attrs}
            return filtered_dic
