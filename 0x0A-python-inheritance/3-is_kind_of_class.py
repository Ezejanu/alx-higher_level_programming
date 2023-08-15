#!/usr/bin/python3
"""This ia a module  that returns True if the object is exactly an instance of
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """Defining the function"""

    if isinstance(obj, a_class):
        return True
    return False
