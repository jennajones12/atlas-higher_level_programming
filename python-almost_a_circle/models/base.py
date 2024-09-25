#!/usr/bin/python3
"""File for class Base"""


class Base:
    """Base class for shapes"""

    id = 0
    __nb_objects = 0

    def __init__(self, id=None):
        """base init funct"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
