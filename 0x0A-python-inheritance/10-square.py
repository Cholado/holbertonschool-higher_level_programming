#!/usr/bin/python3
"""
Double External Module - BaseGeometry
External Module - Rectangle
Module - Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    subclass - Square, inherits from subclass Rectangle
    """
    def __init__(self, size):
        """
        attribute - size
        Initialize private instance attribute size
        and validates that the attribute is an integer greater than 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
