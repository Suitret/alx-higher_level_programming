#!/usr/bin/python3
def uppercase(string):
    for i in string:
        asc = ord(i)
        asc = chr(asc-32) if asc >= 97 and asc <= 122 else chr(asc)
        print("{}".format(asc), end='')
    print("")
