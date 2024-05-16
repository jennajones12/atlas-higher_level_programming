#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """New rectangle class with size attributes."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height) if self.width != 0 and self.height != 0 else 0
    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return("")

        r = []
        for i in range(self.__height):
            [r.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """ Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when a Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
