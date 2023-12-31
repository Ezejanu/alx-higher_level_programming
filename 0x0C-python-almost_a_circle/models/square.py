#!/usr/bin/python3
"""This is a child class Square"""
import sys
from models.rectangle import Rectangle


class Square(Rectangle):
    """This Square class inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """This creates an instance of a square with width, height, x, y"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y}" f" - {self.width}"

    @property
    def size(self):
        """The getter for the width private instance attribute"""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """The setter for the width private instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """updates the value of a rectangle"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
