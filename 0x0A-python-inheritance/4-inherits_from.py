#!/usr/bin/python3
"""This ia a module  that returns True if the object is exactly an instance of
the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """Defining the function"""

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
