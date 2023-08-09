#!/usr/bin/python3
""" This is a function to print a square """


def print_square(size):
    """ This function prints a square with the character # """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size + 1):
        print("#" * size)
