#!/usr/bin/python3

def uniq_add(my_list=[]):

    if not my_list:
        return None

    my_set = set(my_list)
    result = 0

    for val in my_set:
        result += val
    return result
