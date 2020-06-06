#!/usr/bin/python3
"""
Module - "Base" class
"""

class Base:
    """
    class - Base
    private class attribute - nb (number of instantiated bases)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        public class attribute - id
        Initialize base class with public instance attribute id
        count each initialization for nb
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
