#!/usr/bin/python3
x = True
for i in range(ord('z'), ord('a') - 1, -1):
    if x:
        print("{:c}".format(i), end="")
        x = False
    else:
        c = i
        c -= 32
        print("{:c}".format(c), end="")
        x = True
