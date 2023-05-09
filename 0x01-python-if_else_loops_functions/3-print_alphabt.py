#!/usr/bin/python3
for i in range(97, 123):
    char = chr(i)
    if char != 'q' and char != 'e':
        print("{}".format(char), end='')
