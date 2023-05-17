#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary or len(a_dictionary) == 0:
        return None

    key_list = list(a_dictionary)
    best = a_dictionary[key_list[0]]

    for key in key_list:
        if a_dictionary[key] > best:
            best = a_dictionary[key]
    return best
