#!/usr/bin/python3
"""
definition of the Student class.
"""


class Student:
    """
    class representing a student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize Student instance with first name, last name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets dictionary representation of Student instance."""
        return self.__dict__
