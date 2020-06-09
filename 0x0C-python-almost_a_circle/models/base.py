#!/usr/bin/python3
"""
Module - "Base" class
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        public method - to_json_string
        JavaScript Object Notation
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        public method - from_json_string
        JavaScript Object Notation
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        public class method - save_to_file
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        lo = []
        if list_objs is not None:
            for i in list_objs:
                lo.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lo))

    @classmethod
    def create(cls, **dictionary):
        """
        public class method - create
        returns an instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        public class method - load_from_file
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls.from_json_string(f.read())
            for i, e in enumerate(l):
                l[i] = cls.create(**l[i])
        except:
            pass
        return l
