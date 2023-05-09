#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            if i*j < 72:
                print("{}{}".format(i, j), end=", ")
            else:
                if i*j == 72:
                    print("{}{}".format(i, j), end="\n")
