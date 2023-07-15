#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
#        [[column[i] for column in matrix] for i in range(len(column))]

        for row in matrix:
            for column in row:
                print("{:d}".format(column), end=" ")
            print()
