#!/usr/bin/python3
"""File for class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """Initialize width, height, x, y, and id"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints rectangle"""

        for y in range(0, self.__y):
            print()
        for h in range(0, self.__height):
            print(" " * self.__x, end="")
            for w in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """print out rectangle"""
        s = "[" + type(self).__name__ + "] (" + str(self.id) + ") "
        s += str(self.__x) + "/" + str(self.__y) + " - "
        if type(self).__name__ == "Rectangle":
            s += str(self.__width) + "/" + str(self.__height)
        else:
            s += str(self.__width)
        return s
