#!/usr/bin/python3

def safe_print_integer(value):
    if value is None:
        return (0)
    try:
        print("{:d}".format(value))
        return True

    except (ValueError, TypeError):
        return False
