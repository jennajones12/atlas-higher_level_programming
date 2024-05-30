#!/usr/bin/python3
"""defines square, subclass of rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Square class that inherits from Rectangle class.
    represents square with a given size.
    """
    def __init__(self, size):
        self.integer_validator(size)
        super().__init__(size, size)
        self.__size = size

    def integer_validator(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be greater than 0")

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
