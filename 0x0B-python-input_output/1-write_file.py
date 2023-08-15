#!/usr/bin/python3
"""Function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string into a text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to write into the file.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
