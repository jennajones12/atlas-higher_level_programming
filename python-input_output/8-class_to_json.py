#!/usr/bin/python3
"""
function that returns dictionary description with 
simple data structure for JSON serialization of obj
"""


def class_to_json(obj):
    """Returns dictionary descript with data structure
    for JSON serialization of obj
    
    Args:
        obj (object): instance of a Class
    
    Returns:
        dict: dictionary of obj's attributes
    """
    return obj.__dict__
