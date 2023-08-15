#!/usr/bin/python3
"""Function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from JSON file."""
    with open(filename, "r") as a_file:
        return json.load(a_file)
