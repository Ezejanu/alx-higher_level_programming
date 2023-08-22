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
