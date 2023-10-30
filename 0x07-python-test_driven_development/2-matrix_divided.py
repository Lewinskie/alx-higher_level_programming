#!/usr/bin/python3
"""
Module Matrix_divided
Divided matrix
"""

def matrix_divided(matrix, div):
        """
        Returns a matrix of results of a divided matrix
        """
        if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
             raise TypeError("Matrix must be a matrix (list of lists) of \integers/floats")
        for x in matrix:
             if len(x) == 0:
                 raise TypeError("Matrix must b a matrix (list of lists) of \integers/floats")
        lr = []
        for x in matrix:
            lr.append(len(x))
        if not all(item == lr[0] for item on lr):
            raise TypeError("Each roe of thr matrix must have the same size"

        if type(div) != int and type(div) != float:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")
        num = [[round(x /div, 2) for x in y] for y in matrix]
        return num


