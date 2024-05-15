#!/usr/bin/python3


class Square:
    """
    Defines a square


    Private instance attribute:
        size: size of square


    Instantiation with optional size:
        def __init__(self, size=0):


    """

    def __init__(self, size=0):
        """

        Initializes the Square instance


        Args:
            size: (:obj: 'int', optional): A private instance size


        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
