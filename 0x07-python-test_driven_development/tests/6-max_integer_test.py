#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def check(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(list), max(list))


if __name__ == "__main__":
    unittest.main()
