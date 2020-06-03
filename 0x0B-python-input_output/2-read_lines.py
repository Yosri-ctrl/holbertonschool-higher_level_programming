#!/usr/bin/python3
"""
Read n lines from a file
"""


def read_lines(filename="", nb_lines=0):
    """
    read n lines in a text file
    """
    with open(filename, 'r') as f:
        if nb_lines > 0:
            for line in (f.readlines() [0: nb_lines]):    
                print(line, end="")
        else:
            for line in f:
                print(line, end="")
            print()
