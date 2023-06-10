#!/usr/bin/python3
"""Module to compute the
   multiplication of 2 matrixes
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        The resulting matrix after multiplication.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    msg = "m_a should contain only integers or floats"

    for row in m_a:
        if not all(isinstance(cell, (int, float)) for cell in row):
            raise TypeError(msg)

    msg = "m_b should contain only integers or floats"

    for row in m_b:
        if not all(isinstance(cell, (int, float)) for cell in row):
            raise TypeError(msg)

    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    cols_a = len(m_a[0])
    cols_b = len(m_b[0])

    if cols_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(cols_b)] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(cols_b):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
