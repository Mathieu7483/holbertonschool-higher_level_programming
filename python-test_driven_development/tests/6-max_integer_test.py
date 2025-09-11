#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''Test cases for max integer function'''

    def test_max_begin(self):
        self.assertEqual(max_integer([4, 2, 3 , 1]), 4)

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3 , 4]), 4)

    def test_max_mid(self):
        self.assertEqual(max_integer([12, 15, 25, 10]), 25)

    def test_empty(self):
        self.assertEqual(max_integer([]))

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]) -3)

    def test_oneelement(self):
        self.assertEqual(max_integer([-3]) -3)

if __name__ == '__main__':
    unittest.main()