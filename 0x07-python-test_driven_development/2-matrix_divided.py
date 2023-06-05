#!/usr/bin/python3
"""Module which contains matrix_divided
   function
"""


def matrix_divided(matrix, div):
    """function that divides every value
       of a matrix
    Args:
        matrix : the matrix
        div (int/float): divisor
    Returns:
        new matrix
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if isinstance(matrix, list):
        for row in matrix:
            if isinstance(row, list):
                for c in row:
                    if isinstance(c, (int, float)):
                        continue
                    else:
                        raise TypeError(msg)
            else:
                raise TypeError(msg)
    else:
        raise TypeError(msg)

    if len(matrix) == 0:
        raise TypeError(msg)

    msg = "Each row of the matrix must have the same size"

    size = len(matrix[0])

    for row in matrix:
        if len(row) != size:
            raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []

    for row in matrix:
        temp = []
        for cell in row:
            temp.append(rounded(cell/div, 2))
        new_list.append(temp)

    return new_list
