#!/usr/bin/python3
""" This is a module to  add two integers """

def add_integer(a, b=98):
    """The add_integer takes two arguments a and b"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
