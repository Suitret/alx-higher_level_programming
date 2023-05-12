#!/usr/bin/python3
def print_list_integer(my_list=[]):
    lenght = len(my_list)
    for i in range(-1, -(lenght+1), -1):
        print("{:d}".format(my_list[i]))
