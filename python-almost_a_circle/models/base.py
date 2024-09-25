#!/usr/bin/python3
"""File for class Base"""

import json


class Base:
    """Base class for shapes"""

    id = 0
    __nb_objects = 0

    def __init__(self, id=None):
        """base init funct"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_of_dictionaries):
        """Converts list of dicts to json str"""
        if list_of_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_of_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON str representation of list_objs to file"""
        filename = f"{cls.__name__}.json"
        list_dicts = []

        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as json_file:
            json_file.write(json_string)
