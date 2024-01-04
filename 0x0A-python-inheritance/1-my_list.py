#!/usr/bin/python3

class MyList(list):
    """A subclass of list that provides additional functionality.
    
    This class inherits from the built-in list class and adds a method to print
    the elements of the list in sorted order.
    """
    def print_sorted(self):
        """printd out the list in sorted order"""
        sorted_list = sorted(self)
        print (sorted_list)
