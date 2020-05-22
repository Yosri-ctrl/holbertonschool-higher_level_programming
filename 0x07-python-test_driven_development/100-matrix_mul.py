#!/usr/bin/python3
def matrix_mul(m_a, m_b):
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
        if m_a == None or i == None:
            raise ValueError("m_a can't be empty")
        if len(i) != row_size_a:
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if type(j) not in [float, int]:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        if type(i) != list:
            raise TypeError("m_b must be a list of lists")
        if m_b == None or i == None:
            raise ValueError("m_b can't be empty")
        if len(i) != row_size_b:
            raise TypeError("each row of m_b must be of the same size")
        for j in i:
            if type(j) not in [float, int]:
                raise TypeError("m_b should contain only integers or floats")
    
    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            print("j=", m_a[i][j])