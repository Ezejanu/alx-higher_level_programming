#!/usr/bin/python3
def number_keys(a_dictionary):
    if not a_dictionary:
        return 0
    elif a_dictionary:
        number_of_keys = len(list(a_dictionary))
    return number_of_keys
