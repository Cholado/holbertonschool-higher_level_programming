#!/usr/bin/python3
"""
Module - BaseGeometry
Module - Rectangle
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


class Rectangle(BaseGeometry):
    """
    Subclass - Rectangle, inherits from class BaseGeometry
    """
    def __init__(self, width, height):
        """
        attribute - width
        attribute - height
        Initialize private instance attributes width and height
        and validates that both attributes are integers greater than 0
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """
        attribute - area
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        informal string representation of the subclass rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
