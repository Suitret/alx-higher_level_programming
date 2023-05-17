#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return None

    new = [[x**2 for x in sublist] for sublist in matrix]
    return new
