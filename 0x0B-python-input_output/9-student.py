#!/usr/bin/python3
"""A new class called Student."""


class Student:
    """A Student class."""
    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a student class."""
        return self.__dict__
