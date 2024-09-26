#!/usr/bin/python3
"""defines the is_kind_of_class funct"""

def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of or inherits from a_class"""
    return (isinstance(obj, a_class))
