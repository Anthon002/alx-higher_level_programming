#!/usr/bin/python3
""" this module defines the unitteset for the base class
    
    Unittest classes:
    TestBase_initial
"""
import unittest
import os
from models.base import Base
#from models.rectangle import Rectangle
#from models.square import Square

class TestBaase_initial(unittest.TestCase):
    """ This is the test class for the initial base """
    def test_empty_argument(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_None_arg(self):
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_with_arg(self):
        obj1 = Base(2)
        obj2 = Base(4)
        self.assertEqual(2, obj1.id)

    def test_increament(self):
        obj1 = Base(12)
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(7, obj3.id)

    def test_call_private(self):
        a = Base()
        with self.assertRaises(AttributeError):
            print(a.__nb_instances)

    def test_str_arg(self):
        self.assertEqual("32", Base("32").id)
    
    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base(2,5)
