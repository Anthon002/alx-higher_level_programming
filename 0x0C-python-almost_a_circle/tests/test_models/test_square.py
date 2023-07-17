#!/usr/bin/python3
""" This module contains the square class """

import io
import sys
import unittest
from models.base import Base
from models.square import Square

class Test_Square_init(unittest.TestCase):
    """Unit test class to test instantiation of the class Square."""

    def test_1(self):
        self.assertIsInstance(Square(3), Base)

    def test_2(self):
        self.assertIsInstance(Square(3), Square)

    def test_3(self):
        with self.assertRaises(TypeError):
            Square()

    def test_4(self):
        s1 = Square(5)
        s2 = Square(7)
        self.assertEqual(s1.id, s2.id - 1)

    def test_5(self):
        s1 = Square(5, 2)
        s2 = Square(2, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_6(self):
        s1 = Square(5, 2, 4)
        s2 = Square(4, 2, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_7(self):
        self.assertEqual(9, Square(5, 2, 2, 9).id)

class Test_size(unittest.TestCase):
    """Unit test to test the size initialization of the class Square ."""

    def test_1(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("23")

    def test_3(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.14)

    def test_4(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_5(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 12, "b": 21})

    def test_6(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_7(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 5, 13])

class Test_x(unittest.TestCase):
    """Unit test to test the initialization of Square x attr."""

    def test_1(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, None)

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, "7")

    def test_3(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, 3.14)

    def test_4(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, complex(5))

    def test_5(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, {"a": 1, "b": 2})

    def test_6(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, True)

    def test_7(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, [1, 2, 3])

class Test_y(unittest.TestCase):
    """Unit test to test for the initialization of y coordinate."""

    def test_1(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 3, None)

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 3, "7")

    def test_3(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 3, 3.14)

    def test_4(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 3, complex(5))

    def test_5(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 3, {"a": 1, "b": 2})

    def test_6(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 3, [1, 2, 3])

    def test_7(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 3, {1, 2, 3})

class Test_Square_initialization_order(unittest.TestCase):
    """Unittests for verifying the order of Square attribute initialization."""

    def test_1(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("not valid size", "not valid x")

    def test_2(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("not valid size", 1, "not valid y")

    def test_3(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "not valid x", "not valid y")


class Test_area_of_Square(unittest.TestCase):
    """Unittests for verifying the area method of the Square class."""

    def test_1(self):
        self.assertEqual(81, Square(9, 0, 0, 2).area())

    def test_2(self):
        s = Square(123456789, 0, 0, 3)
        self.assertEqual(15241578750190521, s.area())

    def test_3(self):
        s = Square(5, 0, 0, 4)
        s.size = 10
        self.assertEqual(100, s.area())

    def test_4(self):
        s = Square(7, 5, 2, 5)
        with self.assertRaises(TypeError):
            s.area(2)

class TestSquareStrDisplay(unittest.TestCase):
    """Unittests for verifying __str__ and display methods of Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square to print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_1(self):
        s = Square(7)
        capture = TestSquareStrDisplay.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 7\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_2(self):
        s = Square(12, 8)
        correct = "[Square] ({}) 8/0 - 12".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_3(self):
        s = Square(15, 4, 5)
        correct = "[Square] ({}) 4/5 - 15".format(s.id)
        self.assertEqual(correct, str(s))

    def test_4(self):
        s = Square(9, 7, 2, 9)
        self.assertEqual("[Square] (9) 7/2 - 9", str(s))

    def test_5(self):
        s = Square(13, 0, 0, [4])
        s.size = 20
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 20", str(s))

    def test_6(self):
        s = Square(5, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)


class TestSquareUpdateArgs(unittest.TestCase):
    """Unittests for verifying update args method of Square class."""

    def test_1(self):
        s = Square(15, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 15", str(s))

    def test_2(self):
        s = Square(15, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 15", str(s))

    def test_3(self):
        s = Square(15, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_4(self):
        s = Square(15, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_5(self):
        s = Square(15, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_6(self):
        s = Square(15, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_7(self):
        s = Square(15, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_8(self):
        s = Square(15, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittests for verifying update kwargs method of Square class."""

    def test_1(self):
        s = Square(15, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 15", str(s))

    def test_2(self):
        s = Square(15, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_3(self):
        s = Square(15, 10, 10, 10)
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    def test_4(self):
        s = Square(15, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_5(self):
        s = Square(15, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_6(self):
        s = Square(15, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_7(self):
        s = Square(15, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 15".format(s.id)
        self.assertEqual(correct, str(s))


class TestSquareToDictionary(unittest.TestCase):
    """Unittests for verifying to_dictionary method of Square class."""

    def test_1(self):
        s = Square(15, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 15, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_2(self):
        s1 = Square(15, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_3(self):
        s = Square(15, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

