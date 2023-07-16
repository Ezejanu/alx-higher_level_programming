#!/usr/bin/env python3
def no_c(my_string):
    if my_string:
        for i in range(len(my_string)):
            if my_string[i] != 67 and my_string[i] != 99:
                return my_string
