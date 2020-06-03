#!/usr/bin/python3
"""
Module - number_of_lines function
"""


def number_of_lines(filename=""):
    """returns the number of lines of a unicode text file"""
    with open(filename, 'r', encoding='utf8') as f:
        i = 0
        for line in f:
            i += 1
        return i
