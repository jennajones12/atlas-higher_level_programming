#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self):
        """nonexistent"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates parameter as an integer
        
            args:
                name: string, name of parameter
                value: int, parameter to validate
            raises:
                TypeError: if value is not an integer
                ValueError: if value is <= 0
                """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
