#!/usr/bin/python3
"""
Module - "append_wrtie" function
"""


def append_write(filename="", text=""):
    """
    returns the number of unicode chars appended
    to "filename" from "text"
    """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
