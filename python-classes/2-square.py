#!/usr/bin/python3


class Square:
    """Defines a square that has attributes. Instantiation with size

    Attributes:
        size: size of square
    """
    def __init__(self, size=0):
        """Initializes the Square instance

        Args:
            size: (:obj: 'int', optional): A private instance size

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
