#!/usr/bin/python3
"""
function to convert an object to its JSON string representation
"""

import json

def to_json_string(my_obj):
    """
    Returns JSON representation of an object

    Args:
        my_obj: object to convert to JSON

    Returns:
        str: JSON str representation of object
    """
    return json.dumps(my_obj)
