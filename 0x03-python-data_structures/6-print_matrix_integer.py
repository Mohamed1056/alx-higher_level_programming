#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for row in i:
            print("{:d}".format(row), end=" " if row != i[-1] else"")
        print()
