#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Reads a text file."""

    with open(filename, "r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
