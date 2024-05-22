#!/usr/bin/python3
"""class-checking function"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class.

    Args:
        obj: An object to check.
        a_class: A class to compare against.

    Returns:
        True if obj is match, otherwise False. """
    return type(obj) is a_class
