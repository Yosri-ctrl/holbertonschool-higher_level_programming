#!/usr/bin/python3
"""
Matrix Multiplication
"""


def matrix_mul(m_a, m_b):
    """
    multiple two matrix withe different size
    exemple:
    A = [[1, 2], [2, 3]] * [[1, 2], [2, 3]]
    A = [[7, 10], [15, 22]]

    B = [[1, 1]] * [[1, 1]]
    B = [1, 1]
    """
    new = []
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
    a = len(m_a)
    b = len(m_a[0])
    c = len(m_b)
    d = len(m_b[0])
    if b != c:
        raise ValueError("m_a and m_b can't be multiplied")
    new = [[0 for i in range(d)] for j in range(a)]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new[i][j] += m_a[i][k] * m_b[k][j]
    return new
