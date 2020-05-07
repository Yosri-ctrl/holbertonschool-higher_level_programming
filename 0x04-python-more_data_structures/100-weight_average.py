#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return None
    sum = 0
    tota = 0
    for i, j in my_list:
        sum += i * j
        tota += j
    return sum / tota
