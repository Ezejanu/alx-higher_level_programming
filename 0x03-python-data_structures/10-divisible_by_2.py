#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        return_list = my_list.copy()
        for i, value in enumerate(return_list):
            if value % 2 == 0:
                return_list[i] = True
            else:
                return_list[i] = False
        return return_list
