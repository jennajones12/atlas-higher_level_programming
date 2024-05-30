#!/usr/bin/python3
"""
definition of the Student class
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

    
    def to_json(self, attrs=None):
        """
        gets dict representation of Student instance

        Args:
            attrs (list): list of attribute names to get
                If exists, only attributes in this list included
                If None, all attributes included

        Returns:
            dict: dictionary representation of Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}


    def reload_from_json(self, json):
        """
        Replaces attributes of Student instance with values from dict

        Args:
            json (dict): dictionary of attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
