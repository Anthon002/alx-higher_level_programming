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
            Rectangle(2, None)

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "invalid")

    def test_3(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 5.5)

    def test_4(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(5))

    def test_5(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 2, "b": 2})

    def test_6(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [2, 2, 2])

    def test_7(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {2, 2, 2})
