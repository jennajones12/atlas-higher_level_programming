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
       __position (tuple): Position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square instance.

        Args:
            size (int): The size of the square (must be an integer and >= 0).
            position (tuple): The position of the square (must be a tuple of 2 positive integers).

        Raises:
            TypeError: If size is not an integer or position is not a tuple.
            ValueError: If size is less than 0 or position contains non-positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position of the square (must be a tuple of 2 positive integers).

        Raises:
            TypeError: If value is not a tuple.
            ValueError: If value contains non-positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.__position[0] + "#" * self.size)
