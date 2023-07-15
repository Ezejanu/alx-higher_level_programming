#!/usr/bin/env python3
def no_c(my_string):
    if my_string:
        for i in range(len(my_string)):
            if my_string[i] == 'C' or my_string[i] == 'c':
                my_string.pop(my_string[i])
        return my_string
