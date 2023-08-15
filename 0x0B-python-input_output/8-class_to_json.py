#!/usr/bin/python3
"""Function that returns dictionary description of an object."""


def class_to_json(obj):
    """Return dictionary description of obj."""
    return obj.__dict__
