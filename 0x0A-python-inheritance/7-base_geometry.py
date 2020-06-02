#!/usr/bin/python3
"""
Module - BaseGeometry class
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        attribute - area
        Public instance method that raises an Exception when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        attribute - integer_validate
        Public instance method that Validates that value is an integer
        greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
