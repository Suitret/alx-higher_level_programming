#!/usr/bin/python3
import sys


if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    sum = 0

    for arg in argv:
        sum += int(arg)
    print(sum)
