#!/usr/bin/python3
"""
Module - "wrtie_file" function
"""


def write_file(filename="", text=""):
    """
    returns the number of unicode chars written
    to "filename" from "text"
    """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
