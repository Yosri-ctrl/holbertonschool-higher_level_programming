#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in my_list:
        if i == idx:
            new.append(element)
        else:
            new.append(i)
    return new
