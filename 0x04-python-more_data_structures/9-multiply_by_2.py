#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    if not a_dictionary:
        return a_dictionary

    new_dict = dict((key, value*2) for key, value in a_dictionary.items())
    return new_dict
