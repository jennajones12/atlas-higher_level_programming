#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """A class that inherits from list and provides additional functionality"""
    def __init__(self, initial_list=None):
        """Initializes the object with an optional initial list."""
        if initial_list is None:
            super().__init__()
        else:
            super().__init__(initial_list)

    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        print(sorted(self))
