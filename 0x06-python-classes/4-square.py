#!/usr/bin/python3
""" This function defines a class Square """


class Square:
    """This is an class square containing size"""

    def __init__(self, size=0):
        """Initialising the instance variable"""

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
