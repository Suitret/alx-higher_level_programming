#!/usr/bin/python3
for i in range(97, 123):
    if i % 2 == 0:
        char = chr(i)
    else:
        char = chr(i - 32)
    print("{}".format(char), end='')
