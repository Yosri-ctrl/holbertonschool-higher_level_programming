#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            new.append(element)
        else:
            new.append(my_list[i])
    return new
