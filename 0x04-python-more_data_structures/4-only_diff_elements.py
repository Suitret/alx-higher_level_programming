#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    if not set_1 and not set_2:
        return []
    elif not set_1:
        return list(set_2)
    elif not set_2:
        return list(set_1)

    set_3 = set_1 ^ set_2
    return set_3
