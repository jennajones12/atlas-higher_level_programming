#!/usr/bin/python3
"""Class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: An object to check.
        a_class: A class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclass, otherwise False. """
    return isinstance(obj, a_class)
