#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenght = len(my_list)
    if idx < 0 or idx >= lenght:
        cp_list = my_list
        return cp_list
    else:
        cp_list = []
        for i in range(lenght):
            if i != idx:
                cp_list.append(my_list[i])
            else:
                cp_list.append(element)
        return cp_list
