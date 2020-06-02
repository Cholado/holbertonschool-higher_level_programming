#!/usr/bin/python3
"""
External Module - BaseGeometry
Module - Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        return "[Rectangle] {:d}/{:d}.format(self.__width, self.__height)
