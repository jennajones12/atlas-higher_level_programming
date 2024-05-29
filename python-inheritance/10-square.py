#!/usr/bin/python3
"""Square class from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class from Rectangle."""

    def __init__(self, size):
        """Initialize square with size.

        Args:
            size (int): size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate area of the square.

        Returns:
            int: area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """Return strin of square.

        Returns:
            str: string of square.
        """
        return f"[Square] {self.__size}/{self.__size}"
