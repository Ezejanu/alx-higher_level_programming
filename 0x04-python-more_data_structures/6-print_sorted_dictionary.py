#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sorted_keys = sorted(a_dictionary.keys())
        sorted_dictionary = {key: a_dictionary[key] for key in sorted_keys}
        return sorted_dictionary
    return None
