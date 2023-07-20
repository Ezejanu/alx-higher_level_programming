#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sorted_keys = sorted(a_dictionary)
        sorted_dictionary = {i: a_dictionary[i] for i in sorted_keys}
        for key, value in sorted_dictionary.items():
            print("{}: {}".format(key, value))
    return None
