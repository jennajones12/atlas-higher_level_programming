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
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """Get size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of square, updates width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        if kwargs is not None and args is not None:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dict description of shape"""
        d = {"id": self.id,
             "size": self.width,
             "x": self.x,
             "y": self.y}
        return d
