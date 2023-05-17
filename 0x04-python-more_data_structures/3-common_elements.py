#!/usr/bin/python3

def common_elements(set_1, set_2):

    if not set_1 or not set_2:
        return None

    set_3 = set_1 & set_2
    return set_3
