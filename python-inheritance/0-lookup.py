#!/usr/bin/python3
"""
    This module provides a function to retrieve the attributes and methods
    of any given object.
"""


def lookup(obj):
    """Return a list of available attributes and methods of provided obj."""
    return dir(obj)
