#!/usr/bin/python3
def common_elements(set_1, set_2):
    same_elements = {x for x in set_1 if x in set_2}
    return same_elements
