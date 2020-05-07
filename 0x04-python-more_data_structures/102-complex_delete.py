#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for i, j in a_dictionary.items():
        if value == j:
            new.append(i)
    for i in new:
        del a_dictionary[i]
    return a_dictionary
