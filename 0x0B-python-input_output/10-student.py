#!/usr/bin/python3
"""A new class called Student."""


class Student:
    """A Student class."""
    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    def to_json(self, attrs=None):
        if (type(attrs) == list and
                all(type(s) == str for s in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
