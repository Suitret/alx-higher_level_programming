#!/usr/bin/python3

def max_integer(my_list=[]):
    len_ = len(my_list)
    if len_ == 0:
        return None
    else:
        max = my_list[0]
        for i in range(len_):
            if my_list[i] > max:
                max = my_list[i]
        return max
