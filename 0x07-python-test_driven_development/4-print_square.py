#!/usr/bin/python3
"""Module which contains print_square
   function
"""


def print_square(size):
    """function that prints a square
    Args:
        size : the size
    Returns:
        void
    """
    msg = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError(msg)

    if isinstance(size, float) and size < 0:
        raise TypeError(msg)

    if size <= 0:
        raise ValueError("size must be >= 0")

    size = int(size)
    line = '#' * size
    for _ in range(size):
        print(line)
