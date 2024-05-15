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
            size (int): size of the square (default is 0)


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


if __name__ == "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)


    try:
        print(my_square_1.size)
    except Exception as e:
            print(e)


    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    
    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    
    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)
