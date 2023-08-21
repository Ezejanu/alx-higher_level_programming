#!/usr/bin/bash
"""This is a file containing a base class"""


class Base:
    """This is the base class which will be inherited by its subclass"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
