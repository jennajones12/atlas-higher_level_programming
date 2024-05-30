#!/usr/bin/python3
"""
function to write object to txt file using JSON rep
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes object to txt file using JSON

    Args:
        my_obj: object to serialize and write to file
        filename (str): name of file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
