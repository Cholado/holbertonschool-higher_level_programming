#!/usr/bin/python3
"""
Module - "from_json_string" function
"""

import json


def from_json_string(my_str):
    """
    JSON - JavaScript Object Notation
    returns an object represented by a JSON string
    """
    return json.loads(my_str)
