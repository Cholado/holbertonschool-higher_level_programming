#!/usr/bin/python3
"""
Module - add_integer:
    Supplies function, add_integer(a, b=98)
    Checks if parameters are int
    Returns sum of parameters
"""


def add_integer(a, b=98):
    """
    Checks for valid type input (int), return addition of two numbers
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
