#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        matrix_copy = [row[:] for row in matrix]
        matrix_square = list(map(
            lambda row: list(map(lambda x: x**2, row)), matrix_copy
            ))
        return matrix_square
