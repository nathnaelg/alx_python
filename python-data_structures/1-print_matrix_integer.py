#!/usr/bin/python3


# define a function that prints a matrix of integers
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(4):
            print("{:d}"str.format(i), end=" ")
    print()
