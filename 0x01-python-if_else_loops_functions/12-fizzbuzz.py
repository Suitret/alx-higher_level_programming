#!/usr/bin/python3
def fizzbuzz():
    i = 1
    print(i, end='')
    for i in range(2, 101):
        j = i % 3
        k = i % 5
        print(" ", end='')
        if j == 0:
            print("Fizz", end='')
        if k == 0:
            print("Buzz", end='')
        if j and k:
            print(i, end='')
    print(" ", end='')
