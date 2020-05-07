#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
            new.append(list(j ** 2 for j in i))
    return new
