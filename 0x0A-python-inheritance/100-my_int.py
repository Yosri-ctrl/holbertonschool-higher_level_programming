#!/usr/bin/python3
"""
define MyInt
"""


class MyInt(int):
    """
    reverse != and ==
    """
    def __eq__(self, other):
        return self - other != 0

    def __ne__(self, other):
        return self - other == 0
