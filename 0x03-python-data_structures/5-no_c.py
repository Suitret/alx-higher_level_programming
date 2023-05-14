#!/usr/bin/env python3
def no_c(my_string):
    if not my_string:
        return

    lenght = len(my_string)
    new_string = ""
    for i in range(lenght):
        if my_string[i] not in "cC":
            new_string += my_string[i]
    return new_string
