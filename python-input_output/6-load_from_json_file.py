#!/usr/bin/python3
"""
function to create an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates object from a JSON file

    Args:
        filename (str): The name of the file

    Returns:
        object: Py object represented by JSON file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
