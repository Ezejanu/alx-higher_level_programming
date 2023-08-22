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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        file_name = f"{cls.__name__}.json"
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_list)
        with open(file_name, "w") as json_file:
            json_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or json_string is None:
            return "[]"
        else:
            return json.loads(json_string)
