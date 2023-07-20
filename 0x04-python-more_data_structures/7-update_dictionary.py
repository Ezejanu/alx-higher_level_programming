#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not a_dictionary:
        a_dictionary = {key:value}
    elif a_dictionary:
        if key in a_dictionary:
            a_dictionary[key] = value
        elif key not in a_dictionary:
            a_dictionary[key] = value
    return a_dictionary
