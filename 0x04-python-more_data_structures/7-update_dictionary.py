#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    if not a_dictionary:
        a_dictionary = dict()

    a_dictionary[key] = value
    new_dict = a_dictionary
    return new_dict
