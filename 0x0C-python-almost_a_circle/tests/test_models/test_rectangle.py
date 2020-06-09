#!/usr/bin/python3
"""
test cases for class Rectangle
"""
import unittest as u
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangleClass(u.TestCase):
    """
    testing the class Rectangle
    """
    def test_id(self):
        """test id """
        r1 = Rectangle(10, 2)
        a1 = r1.id
        self.assertEqual(a1, r1.id)

    def test_id_second(self):
        """test id """
        r2 = Rectangle(1, 1, 0, 0, 20)
        a2 = r2.id
        self.assertEqual(a2, 20)

    def test_id_neg(self):
        """test id """
        r3 = Rectangle(10, 2, 5, 3, -8)
        a3 = r3.id
        self.assertEqual(a3, -8)

    def test_width_neg(self):
        """test width"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_width_type(self):
        """test width"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle([1], 2)

    def test_height_neg(self):
        """test height"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_height_type(self):
        """test height"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, [2])

    def test_x_neg(self):
        """test x"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_x_type(self):
        """test x"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "1")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {1})

    def test_y_neg(self):
        """test y"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 1, -2)

    def test_y_type(self):
        """test y"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 1, (1,))

    def test_area(self):
        """test area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 3 * 2)
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r2.area(), 1 * 2)

    def test_display(self):
        """test dispaly"""
        r1 = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "###\n###\n")

    def test_display_with_no_spaces(self):
        """test dispaly"""
        r1 = Rectangle(3, 2, 0, 0)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "###\n###\n")

    def test_display_with_space(self):
        """test dispaly"""
        r1 = Rectangle(3, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "\n ###\n ###\n")

    def test_display_the_one(self):
        """test dispaly"""
        r1 = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), "#\n")

    def test_display_big_space(self):
        """test dispaly"""
        r1 = Rectangle(3, 2, 5, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(),
                             "\n\n\n\n\n\n\n\n\n\n     ###\n     ###\n")

    def test_update(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (10) 10/10 - 10/10\n")

    def test_update_id(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(89)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (89) 10/10 - 10/10\n")

    def test_update_width(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(89, 3)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (89) 10/10 - 3/10\n")

    def test_update_height(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(89, 3, 2)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (89) 10/10 - 3/2\n")

    def test_update_x(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(89, 3, 2, 1)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (89) 1/10 - 3/2\n")

    def test_update_y(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(89, 3, 2, 1, 2)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (89) 1/2 - 3/2\n")

    def test_update_dic_id(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(id=20)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (20) 10/10 - 10/10\n")

    def test_update_dic_width(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(width=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (10) 10/10 - 4/10\n")

    def test_update_dic_height(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(height=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (10) 10/10 - 10/4\n")

    def test_update_dic_x(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(x=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (10) 4/10 - 10/10\n")

    def test_update_dic_y(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(y=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (10) 10/4 - 10/10\n")

    def test_update_dic_more(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(x=1, height=2, y=3, width=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (10) 1/3 - 4/2\n")

    def test_update_dic_random(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(20, 1, x=1, height=2, y=3, width=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (20) 1/3 - 1/2\n")

    def test_update_dic_empty(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update()
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (10) 10/10 - 10/10\n")

    def test_update_dic_full(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.update(4, 2, 2, 1, 1, x=1, height=2, y=3, width=4, id=8)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 1/1 - 2/2\n")

    def test_dictionary(self):
        """test dict"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        c = "{'x': 10, 'y': 10, 'id': 10, 'height': 10, 'width': 10}\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            a1 = r1.to_dictionary()
            print(a1)
            self.assertEqual(fake_out.getvalue(), c)
        self.assertEqual(type(a1), dict)
