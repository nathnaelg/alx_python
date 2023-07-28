#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square = []
    for row in matrix:
        square_row = []
        for i, element in enumerate(row):
            square_row.append(element ** 2)
        square.append(square_row)
    return square
