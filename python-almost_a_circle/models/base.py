#!/usr/bin/python3
"""
Base module
"""


class Base:
    """
    The Base class for all other classes in this project.
    Manages `id` attribute to avoid duplicating the same code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of a Base instance.

        Args:
            id (int): The id of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
