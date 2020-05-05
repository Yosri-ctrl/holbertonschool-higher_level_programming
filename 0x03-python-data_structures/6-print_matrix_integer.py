#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for i in matrix:
        print(" ".join("{:d}".format(j)for j in i))
    #    for j in i:
    #        print(' '.join('{:d}'.format(j)))
