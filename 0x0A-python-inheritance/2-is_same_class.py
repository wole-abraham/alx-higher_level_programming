#!/usr/bin/python3 

"""a function that returns True"""

def is_same_class(obj, a_class):

    """Returns True is obj is instance of class else False"""
    
    if isinstance(obj, a_class):
        return type(obj) is a_class
