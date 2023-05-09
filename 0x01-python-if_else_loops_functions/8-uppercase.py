#!/usr/bin/python3
def uppercase(string):
    lenght = len(string)
    j = 0
    for i in string:
        j += 1
        delim = ''
        if j == lenght:
            delim = '\n'
        asc = ord(i)
        if asc >= 97 and asc <= 122:
            asc = chr(asc - 32)
            print("{}".format(asc), end=delim)
        else:
            asc = chr(asc)
            print("{}".format(asc), end=delim)
