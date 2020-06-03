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
        """
        return self.__dict__
