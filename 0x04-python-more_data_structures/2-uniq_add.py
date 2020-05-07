#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new = []
    for i in my_list:
        if i not in new:
            sum += i
            new.append(i)
    return sum
