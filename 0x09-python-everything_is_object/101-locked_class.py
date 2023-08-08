#!/usr/bin/python3
""" This is a Locked class """


class LockedClass:
    """ A locked class with no attributes """

    def __setattr__(self, name, value):
        if name != "first_name" and not hasattr(self, 'first_name'):
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
