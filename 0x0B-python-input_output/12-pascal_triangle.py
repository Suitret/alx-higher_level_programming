#!/usr/bin/python3
"""Module containing pascal_triangle function
"""


def pascal_triangle(n):
    """function that initializes attributes
        Args:
            n : the size
        Returns:
            list of lists
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        L = [[1], [1, 1]]
        for j in range(n):
            temp = []
            for i in range(n):
                if i == 0 or i == n-1:
                    temp.append(1)
                else:
                    temp.append(L[n-2][i] + L[n-2][i-1])
            L.append(temp)
        return L
