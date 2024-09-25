#!/usr/bin/python3
"""File for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square with size, x, y, and id"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of square, updates width and height"""
        self.width = value
        self.height = value
