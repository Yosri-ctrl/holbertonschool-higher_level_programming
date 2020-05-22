#!/usr/bin/python3
"""
Divide an integer by a const
"""


def matrix_divided(matrix, div):
    """
    take a matrix and divid eche element by div rounded to the closeset 2
    and return a new list
    """
    new = []
    if type(matrix[0]) == list:
        row_size = len(matrix[0])
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if type(i) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
                        integers/floats")
        new.append([round(j / div, 2) for j in i])

    return new
