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
        for j in range(2, n):
            temp = [1]
            pr = L[j-1]
            for i in range(1, j):
                temp.append(pr[i] + pr[i-1])
            temp.append(1)
            L.append(temp)
        return L
