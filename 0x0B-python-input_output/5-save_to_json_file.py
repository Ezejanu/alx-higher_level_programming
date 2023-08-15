#!/usr/bin/python3
"""Function that writes an Object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an objject to a text file in JSON representation.

    Args:
        my_obj (str): The object to be written into the file.
        filename (str): The name of the file to be written into.
    """
    with open(filename, "w") as a_file:
        json.dump(my_obj, a_file)
