#!/usr/bin/python3
"""
Module - class "Student"
"""


class Student:
    """
    class - student
    """
    def __init__(self, first_name, last_name, age):
        """
        attribute - first_name
        attribute - last_name
        attribute - age
        Initializes public instance attributes
        fist name, last name and age of the class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns a dictionary representation of a Student instance
        retrieve specified attributes, or all if not specified
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict
