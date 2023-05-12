#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    len_a, len_b = len(tuple_a), len(tuple_b)

    if len_a < 2:
        a = (0, 0) if len_a == 0 else (tuple_a[0], 0)
    else:
        a = tuple_a

    if len_b < 2:
        b = (0, 0) if len_b == 0 else (tuple_b[0], 0)
    else:
        b = tuple_b

    return (a[0] + b[0]), (a[1] + b[1])
