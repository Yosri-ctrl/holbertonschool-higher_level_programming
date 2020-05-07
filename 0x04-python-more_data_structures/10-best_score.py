#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    maxi = ""
    if a_dictionary is None:
        return None
    for i, j in a_dictionary.items():
        if max < j:
            max = j
            maxi = i
    return maxi
