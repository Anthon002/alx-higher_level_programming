#!/usr/bin/python3
""" This model is the unittest for rectangle class
    
    Unittest classes:
    TestRectangle_init
"""

from models.base import Base
from models.rectangle import Rectangle
import sys
import os
import io
import unittest

class TestRectangle_init(unittest.TestCase):
    """ this is the unittest class for the init in rectangle class"""

    def test_with_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_with_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 12, 33, 44, 75, 1)

    def test_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(51, 15, 30, 23, 1).__width)

    def test_getting_width(self):
        r = Rectangle(1, 2, 3, 4, 1)
        self.assertEqual(1, r.width)

    def test_heightGetterFunc(self):
        r = Rectangle(3, 34, 6, 15, 1)
        self.assertEqual(34, r.height)

    def test_heightSetter_Func(self):
        r = Rectangle(5, 3, 4, 5,1)
        r.height = 13
        self.assertEqual(13, r.height)
class Test_Width(unittest.TestCase):
    """ The Unittest for width attribute of the Rectangle."""

    def test_Width_1(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 12)

    def test_Width_2(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("13", 21)

    def test_Width_3(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(4.15, 31)

    def test_Width_4(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(34), 22)

    def test_Width_5(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(7), 3)

    def test_Width_6(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'unittest', 3)

    def test_Width_7(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'unittest'), 3)

class TestRectangleHeight(unittest.TestCase):
    """Unittests for the height of the rectangle."""

    def test_1(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(12, None)

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(21, "21")

    def test_3(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(22, 4.5)

    def test_4(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(15))

    def test_5(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 1, "b": 3})

    def test_6(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [2, 2, 2])

    def test_7(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {2, 2, 2})
class TestRectangleX(unittest.TestCase):
    """Testing the x coordinates for the rectangle."""

    def test_1(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 21, None)

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(32, 2, "string", 2)

    def test_3(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(22, 12, 3.5, 19)

    def test_4(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(23, 12, complex(45))

    def test_5(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(22, 21, {"a": 12, "b": 1}, 1)

    def test_6(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, True, 12)

    def test_7(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(24, 42, [12, 22, 62], 22)

class TestRectangleY(unittest.TestCase):
    """ Test class for the y coordinate of the rectangle."""

    def test_1(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(12, 22, 13, None)

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(12, 22, 13, "23")

    def test_3(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(12, 22, 13, 4.5)

    def test_4(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(12, 22, 13, complex(3))

    def test_5(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 21, 11, {"a": 3, "b": 12})

    def test_6(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 2, [1, 12, 4])

    def test_7(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 7, 5, {1, 5, 3})


class TestRectagleInitializationOrder(unittest.TestCase):
    """ Unit testing the order of initialization ."""

    def test_1(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("23", "45")

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("23", 2, "34")

    def test_3(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("23", 12, 33, "y")

    def test_4(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(22, "invalid", " x")

    def test_5(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(21, "height", 12, "y")

    def test_6(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(22, 12, "x", "y")

class TestRectangleArea(unittest.TestCase):
    """ Testing the rectangle area"""

    def test_1(self):
        r = Rectangle(11, 2, 0, 0, 0)
        self.assertEqual(22, r.area())

    def test_2(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 2
        r.height = 14
        self.assertEqual(28, r.area())

    def test_3(self):
        r = Rectangle(2, 13, 3, 2, 1)
        with self.assertRaises(TypeError):
            r.area(2)

class Test_Rectangle_args(unittest.TestCase):
    """Unittesting for the update args."""

    def test_1(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update()
        self.assertEqual("[Rectangle] (20) 20/20 - 20/20", str(r))

    def test_2(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(77)
        self.assertEqual("[Rectangle] (77) 20/20 - 20/20", str(r))

    def test_3(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(77, 5)
        self.assertEqual("[Rectangle] (77) 20/20 - 5/20", str(r))

    def test_4(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(77, 5, 10)
        self.assertEqual("[Rectangle] (77) 20/20 - 5/10", str(r))

    def test_5(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(77, 5, 10, 15)
        self.assertEqual("[Rectangle] (77) 15/20 - 5/10", str(r))

    def test_6(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(77, 5, 10, 15, 25)
        self.assertEqual("[Rectangle] (77) 15/25 - 5/10", str(r))

    def test_7(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(77, 5, 10, 15, 25, 30)
        self.assertEqual("[Rectangle] (77) 15/25 - 5/10", str(r))

class Test_Rectangle_kwargs(unittest.TestCase):
    """Unit tests to test update kwargs method of the class Rectangle."""

    def test_1(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(id=2)
        self.assertEqual("[Rectangle] (2) 20/20 - 20/20", str(r))

    def test_2(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(width=5, id=3)
        self.assertEqual("[Rectangle] (3) 20/20 - 5/20", str(r))

    def test_3(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(width=3, height=7, id=4)
        self.assertEqual("[Rectangle] (4) 20/20 - 3/7", str(r))

    def test_4(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(id=5, x=6, height=8, y=9, width=10)
        self.assertEqual("[Rectangle] (5) 6/9 - 10/8", str(r))

    def test_5(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(y=12, x=15, id=7, width=11, height=13)
        self.assertEqual("[Rectangle] (7) 15/12 - 11/13", str(r))

    def test_6(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(id=None)
        correct = "[Rectangle] ({}) 20/20 - 20/20".format(r.id)
        self.assertEqual(correct, str(r))

    def test_7(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(id=None, height=15, y=17)
        correct = "[Rectangle] ({}) 20/17 - 20/15".format(r.id)
        self.assertEqual(correct, str(r))

    def test_8(self):
        r = Rectangle(20, 20, 20, 20, 20)
        r.update(id=5, x=6, height=8)
        r.update(y=9, height=25, width=30)
        self.assertEqual("[Rectangle] (5) 6/9 - 30/25", str(r))


import unittest
import io
import sys

class TestRectangle_stdout(unittest.TestCase):
    """Unittests for __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Capture and return text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle.
            method (str): The method.
        Returns:
            text printed to stdout.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_1(self):
        r = Rectangle(6, 9)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 6/9\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_2(self):
        r = Rectangle(8, 8, 3)
        correct = "[Rectangle] ({}) 3/0 - 8/8".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_3(self):
        r = Rectangle(4, 16, 2, 3)
        correct = "[Rectangle] ({}) 2/3 - 4/16".format(r.id)
        self.assertEqual(correct, str(r))

    def test_4(self):
        r = Rectangle(12, 20, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 12/20", str(r))

    def test_5(self):
        r = Rectangle(8, 8, 0, 0, [4])
        r.width = 16
        r.height = 2
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 16/2", str(r))

