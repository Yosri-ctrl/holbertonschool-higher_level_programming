#!/usr/bin/python3
def roman_to_int(roman_string):
    alpha = {"M": 1000, "D": 500, "C": 100, 
    "L": 50, "X": 10, "V": 5, "I": 1, None: None}
    sum = 0
    for i in roman_string:
        for x, y in alpha.items():
            #if i == "I" and j == x:
            #    sum += y - 1
                
            if x == i:
                sum += y
    return sum
