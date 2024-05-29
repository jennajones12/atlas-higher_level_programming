#!/usr/bin/python3
"""Module for Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inherited from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize ectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of rectangle.

        Returns:
            str: string representation of rectangle.
        """
        return f"[Rectangle] {self.__width} / {self.__height}"
