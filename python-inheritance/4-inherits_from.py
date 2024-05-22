#!/usr/bin/python3
"""Function to check if instance is inherited"""


def inherits_from(obj, a_class):
    """Checks if instance is inherited directly or indirectly from specified class.

    Args:
        obj: An object to check.
        a_class: A class to compare against.

    Returns:
        True if so, otherwise False"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
