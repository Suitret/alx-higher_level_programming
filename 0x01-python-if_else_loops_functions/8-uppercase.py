#!/usr/bin/python3
def uppercase(string):
    for i in string:
        asc = ord(i)
        if asc >= 97 and asc <= 122:
            print("{}".format(asc - 32), end='')
        else:
            print("{}".format(asc), end='')
