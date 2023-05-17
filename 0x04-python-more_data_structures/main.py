#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 1, 1, 1, 1, 1]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
