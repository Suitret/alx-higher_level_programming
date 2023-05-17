#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list or my_list == []:
        return 0

    num, den = 0, 0

    for tuple_ in my_list:
        num += tuple_[0]*tuple_[1]
        den += tuple_[1]

    return num/den
