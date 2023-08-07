#!/usr/bin/python3

""" This is a class that defines a rectangle """


class Rectangle:
    """ This is a class that defines a rectangle """

    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        rectangle_str = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                row = ""
                # Reset row for each new row of the rectangle
                for j in range(self.__width):
                    row += "#"
                rectangle_str += row + "\n"
        return rectangle_str
