#!/usr/bin/python3
def no_c(my_string):

    if 'c' not in my_string and 'C' not in my_string:
        return my_string

    if not my_string:
        return None

    new_string = ""
    for char in my_string:
        if char not in "Cc":
            new_string += char
    return new_string
