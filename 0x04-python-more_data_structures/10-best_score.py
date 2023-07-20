#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sorted_dictionary = sorted(a_dictionary.items())
        return sorted_dictionary[-1][0]
