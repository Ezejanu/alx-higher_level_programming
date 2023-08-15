#!/usr/bin/python3
"""This is a module that adds that adds a new attribute to an object if it’s
possible"""


def add_attribute(obj, attribute_name, value):
    """This defines the function"""

    if not hasattr(obj, attribute_name):
        if (
            hasattr(obj, "__dict__")
            or (hasattr(type(obj), "__dict__") and attribute_name in type(obj).__dict__)
            or hasattr(obj, "__slots__")
        ):
            setattr(obj, attribute_name, value)
    else:
        raise TypeError("can't add new attribute")
