#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    lenght = len(matrix[0])
    width = len(matrix)
    for i in range(width):
        for j in range(lenght):
            print("{:d}".format(matrix[i][j]), end='')
            if j != (lenght-1):
                print(" ", end='')
        print()
