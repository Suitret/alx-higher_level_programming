#!/usr/bin/python3
def uppercase(string):
    for i in string:
        asc = ord(i)
        if asc >= 97 and asc <= 122:
            asc = chr(asc - 32)
            print("{}".format(asc), end='')
        else:
            asc = chr(asc)
            print("{}".format(asc), end='')
