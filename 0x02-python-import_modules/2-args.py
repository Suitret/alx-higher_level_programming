#!/usr/bin/python3
import sys

lenght = len(argv)

if lenght is 0:
    print("0 arguments.")
else:
    if lenght is 1:
        print("1 argument:")
    else:
        print(lenght, "arguments:")

    i = 1
    for arg in argv:
        print("{:d}: {}".format(i, arg))
        i += 1

if __name__ == "__main__":
    main()
