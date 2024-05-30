#!/usr/bin/python3
"""
function to convert JSON string to Python object
"""

import json


def from_json_string(my_str):
    """
    Returns an object represented by JSON str

    Args:
        my_str (str): JSON str to convert

    Returns:
        object: object represented by JSON str
    """
    return json.loads(my_str)
