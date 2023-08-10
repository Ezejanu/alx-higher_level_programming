#!/usr/bin/python3
""" This is a function that prints the first name and last name """

def say_my_name(first_name, last_name=""):
    """ This functions prints a string """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
