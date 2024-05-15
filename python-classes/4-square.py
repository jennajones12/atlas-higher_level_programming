#!/usr/bin/python3
"""
Module square
Defines a class Square.
"""


class Square:
    """
    Defines a square that has attributes. Instantiation with size.

    Attributes:
       __size (int): Size of square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
            size (int): The size of the square (must be an integer and >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square (must be an integer and >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
