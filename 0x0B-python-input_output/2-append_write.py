#!/usr/bin/python3
"""Function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Function that appends to the end of a text file.

    Args:
        filename (str): The name of the file to write into.
        text (str): The string to write into the file.
    Returns:
        The number of characters appended to the end of the file.
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
