#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y, num in enumerate(x):
            print("{:d}".format(num), end=" " if y < len(x) - 1 else "")
        print()
