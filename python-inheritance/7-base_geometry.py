#!/usr/bin/python3
"""documentation"""


class BaseGeometry:
    """documentaiton"""

    def area(self):
        """documentation"""
        e = "area() is not implemented"
        raise Exception(e)

    def integer_validator(self, name, value):
        """is it an integer"""
        e1 = "{} must be an integer"
        e2 = "{} must be greater than 0"
        if (type(value) is not int):
            raise TypeError(e1.format(name))
        if value <= 0:
            raise ValueError(e2.format(name))
