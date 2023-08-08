#!/usr/bin/python3
""" This is a Locked class """


class LockedClass:
    """ A locked class with no attributes """

    __slots__ = ["first_name"]


    def __init__(self):
        self.first_name = None
