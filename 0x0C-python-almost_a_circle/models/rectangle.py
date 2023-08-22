#!/usr/bin/python3
"""This is a child class Rectangle"""
import sys
from models.base import Base


class Rectangle(Base):
    """This Rectangle class inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This creates an instance of a rectangle with width, height, x, y"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter for the width private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter for the width private instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter for the height private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter for the height private instance attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter for x private instance attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter for x private instance attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """The getter for y private instance attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter for y private instance attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Displays(prints) a rectangle using the # character"""
        if self.__width == 0 or self.__height == 0:
            return ""

        """rectangle_str = ""
        for i in range(self.__height):
            row = ""
            for j in range(self.__width):
                row += "#"
            rectangle_str += row
            if i != self.__height - 1:
                rectangle_str += "\n"
        print (rectangle_str)"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
            f" - {self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """updates the value of a rectangle"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
