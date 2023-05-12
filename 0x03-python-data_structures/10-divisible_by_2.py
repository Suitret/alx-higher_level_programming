#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    len_ = len(my_list)
    new_list = []

    if len == 0:
        return new_list
    else:
        for i in range(len_):
            string = True if my_list[i] % 2 == 0 else False
            new_list.append(string)
        return new_list
