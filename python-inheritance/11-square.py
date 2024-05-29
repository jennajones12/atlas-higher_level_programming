#!/usr/bin/python3
"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size):
        """Initializes Square"""
        super().__init__(size, size)

    def __str__(self):
        """String of Square"""
        return "[Square] {}/{}".format(self.__side, self.__height)
