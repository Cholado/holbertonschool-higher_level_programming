#!/usr/bin/python3
"""
Module - "to_json_string" fundtion
"""

import json


def to_json_string(my_obj):
    """
    JSON - JavaScript Object Notation
    returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
