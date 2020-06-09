#!/usr/bin/python3
"""
test cases for class Square
"""
import unittest as u
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(u.TestCase):
    """
    testing the class Square
    """
    def test_square(self):
        s1 = Square(5, id=1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(),
                             "[Square] (1) 0/0 - 5\n")

    def test_square_x(self):
        s1 = Square(5, 1, id=1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(),
                             "[Square] (1) 1/0 - 5\n")

    def test_square_y(self):
        s1 = Square(5, 1, 2, id=1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(),
                             "[Square] (1) 1/2 - 5\n")

    def test_square_area(self):
        s1 = Square(5, id=1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1.area())
            self.assertEqual(fake_out.getvalue(),
                             "25\n")

    def test_square_display(self):
        s1 = Square(2, id=1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(),
                             "##\n##\n")

    def test_size_type(self):
        with self.assertRaises(TypeError):
            Square("2")

    def test_size_value(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_update_square(self):
        s1 = Square(10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.update(4, 2, 2, 1,
                      x=1, y=3, size=4, id=8)
            print(s1)
            self.assertEqual(fake_out.getvalue(),
                             "[Square] (4) 2/1 - 2\n")

    def test_update_square_kwargs(self):
        s1 = Square(10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.update(x=1, y=3, size=4, id=8)
            print(s1)
            self.assertEqual(fake_out.getvalue(),
                             "[Square] (8) 1/3 - 4\n")

    def test_update_square_mix(self):
        s1 = Square(10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.update(4, y=3, size=4, id=8)
            print(s1)
            self.assertEqual(fake_out.getvalue(),
                             "[Square] (4) 10/3 - 4\n")

    def test_dictionary(self):
        s1 = Square(10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            a1 = s1.to_dictionary()
            print(a1)
            self.assertEqual(fake_out.getvalue(),
                             "{'id': 10, 'x': 10, 'y': 10, 'size': 10}\n")
        self.assertEqual(type(a1), dict)
