#!/usr/bin/python3

""" modules prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=''):
    """ says your name """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    return f'My name is {first_name} {last_name}'.strip()
