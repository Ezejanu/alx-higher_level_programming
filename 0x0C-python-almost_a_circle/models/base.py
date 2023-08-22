#!/usr/bin/python3
"""This is a file containing a base class"""
import json


class Base:
    """This is the base class which will be inherited by its subclass"""

    __nb_objects = 0

    def __init__(self, id=None):
        """create an instance of the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
