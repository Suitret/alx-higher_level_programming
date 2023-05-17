#!/usr/bin/python3

def uniq_add(my_list=[]):

    result = 0

    if not my_list:
        return result

    my_set = set(my_list)

    for val in my_set:
        result += val
    return result
