#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """A class that inherits from list and provides additional functionality."""

    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList([3, 1, 2])
    my_list.print_sorted()

