#!/usr/bin/python3
""" This function defines a class Square """


class Square:
    """This is an class square containing size"""

    def __init__(self, size=0):
        """Initialising the instance variable"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
