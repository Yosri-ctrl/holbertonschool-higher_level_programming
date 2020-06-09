#!/usr/bin/python3
"""
test cases for task 0
"""
import unittest as u
from models.base import Base


class TestBaseClass(u.TestCase):
    """
    Test the Base Class
    """
    def test_id_first(self):
        """test id """
        b1 = Base()
        a1 = b1.id
        self.assertEqual(a1, 1)

    def test_id_givin(self):
        """test id """
        b4 = Base(12)
        a4 = b4.id
        self.assertEqual(a4, 12)

    def test_id_second(self):
        """test id """
        b2 = Base()
        a2 = b2.id
        self.assertEqual(a2, 2)

    def test_id_negative(self):
        """test id """
        b3 = Base(-5)
        a3 = b3.id
        self.assertEqual(a3, -5)
