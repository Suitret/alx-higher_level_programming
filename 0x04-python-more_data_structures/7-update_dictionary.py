#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    if not a_dictionary:
        new_dict = dict()

    new_dict[key] = value
    a_dictionary = new_dict
    return new_dict
