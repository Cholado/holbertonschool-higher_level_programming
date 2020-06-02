#!/usr/bin/python3
"""
Module - MyList class
"""


class MyList(list):
    """a subclass of list, that inherits from list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
