#!/usr/bin/python3
"""defines square, subclass of rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size):
        """initializes new square

        size: (int) size of new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def __str__(self):
            return f"[Square] {self.__size}/{self.__size}"
