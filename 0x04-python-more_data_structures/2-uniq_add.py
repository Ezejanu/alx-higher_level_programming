#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        unique_values = set(my_list)
   # print(unique_values)
        total = 0;
        for value in unique_values:
            total += value
        return total
