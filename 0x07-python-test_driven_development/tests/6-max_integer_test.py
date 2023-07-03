#!/usr/bin/python3
"""
This module contains the unitest for max_integer() function
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """list of all the test cases for max_integer()"""

    def test_valid_input(self):
        test_list = [2,4,7,0]
        result = max_integer(test_list)
        self.assertEqual(result, 7)

    def test_same_inputs(self):
        test_list = [4,4,4,4]
        result = max_integer(test_list)
        self.assertEqual(result, 4)

    def test_floats(self):
        test_list = [3.4,4.6,1.2,22.0]
        result = max_integer(test_list)
        self.assertEqual(result, 22.0)

    def test_negative(self):
        test_list = [-2,-1,-7,-9]
        result = max_integer(test_list)
        self.assertEqual(result,-1)

    def test_loop_list(self):
        my_list = [0, 2, 12, 2, 8]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 60)

    def test_one_elemen(self):
        self.assertEqual(max_integer([10]), 10)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '23'])

    def test_tuples(self):
        with self.assertRaises(TypeError):
            max_integer([2, (11, 35)])

    def test_dictionaries_values(self):
        with self.assertRaises(KeyError):
            max_integer({'num1': 10, 'num2': 20})

    def test_number_not_list(self):
        with self.assertRaises(TypeError):
            max_integer(34)
