#!/usr/bin/python3
"""
multiple a matrix using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiple two matrix withe different size
    exemple:
    A = [[1, 2], [2, 3]] * [[1, 2], [2, 3]]
    A = [[7, 10], [15, 22]]

    B = [[1, 1]] * [[1, 1]]
    B = [1, 1]
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if type(m_a) == list and type(m_a[0]) == list:
        row_size_a = len(m_a[0])
    if type(m_b) == list and type(m_b[0]) == list:
        row_size_b = len(m_b[0])

    for i in m_a:
        if type(i) != list:
            raise TypeError("m_a must be a list of lists")
        if len(m_a) == 0 or len(i) == 0:
            raise ValueError("m_a can't be empty")
        if len(i) != row_size_a:
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if type(j) not in [float, int]:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        if type(i) != list:
            raise TypeError("m_b must be a list of lists")
        if len(m_b) == 0 or len(i) == 0:
            raise ValueError("m_b can't be empty")
        if len(i) != row_size_b:
            raise TypeError("each row of m_b must be of the same size")
        for j in i:
            if type(j) not in [float, int]:
                raise TypeError("m_b should contain only integers or floats")
    A = np.array(m_a)
    B = np.array(m_b)
    new = np.matmul(A, B)
    return new
