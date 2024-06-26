#!/usr/bin/python3
"""defines square, subclass of rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents square"""

    def __init__(self, size):
        """initializes new square

        size: (int) size of new square
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

