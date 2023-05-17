#!/usr/bin/python3

def search_replace(my_list, search, replace):

    if (not my_list) or (search not in my_list):
        return my_list

    new_list = []

    for val in my_list:
        if val == search:
            new_list.append(replace)
        else:
            new_list.append(val)

    return new_list
