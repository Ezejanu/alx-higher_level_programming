#!/usr/bin/python3
""" This function defines a class Square """


class Square:
    """This is an class square containing size"""

    def __init__(self, __size=0):
        """Initialising the instance variable"""

        if not isinstance(__size, int):
            raise TypeError("Size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")

        self.__size = __size

    def area(self):
        return self.__size ** 2
