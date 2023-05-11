#!/usr/bin/python3
import sys


if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    else:
        if argc == 1:
            print("1 argument:")
        else:
            print(argc, "arguments:")

        i = 1
        for arg in argv:
            print("{:d}: {}".format(i, arg))
            i += 1
