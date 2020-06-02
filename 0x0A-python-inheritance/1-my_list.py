#!/usr/bin/python3
"""
define Mylist a subcalss for list
"""


class Mylist(list):
    """
    print a sorted list of list
    """
    def print_sorted(self):
        print(sorted(self)
