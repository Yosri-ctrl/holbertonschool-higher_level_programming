#!/usr/bin/python3
def roman_to_int(roman_string) -> int:
    alpha = {"M": 1000, "D": 500, "C": 100, 
    "L": 50, "X": 10, "V": 5, "I": 1}
    sum = 0
    for i in range(len(roman_string)):
        for x, y in alpha.items():
            #if roman_string[i] == "I":
            #    sum += y - 1
                
            if x == roman_string[i]:
                sum += y
    return sum
