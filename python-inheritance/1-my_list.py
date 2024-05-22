#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """A class that inherits from list and provides additional functionality."""
    def __init__(self):
         """initializes the object"""
         super().__init__()

    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        print(sorted(self))
