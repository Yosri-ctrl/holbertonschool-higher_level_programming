#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ch =ord(i)
        if ord(i) >= 97 and ord(i) <= 122:
            ch = ord(i) - 32

        print("{:c}".format(ch), end="")
    print()
