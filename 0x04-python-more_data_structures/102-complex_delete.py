#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if not a_dictionary:
        return a_dictionary

    del_list = list(a_dictionary)

    for key in del_list:
        if a_dictionary[key] == value:
            del a_dictionary[key]

    return a_dictionary
