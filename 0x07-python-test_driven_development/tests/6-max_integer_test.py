#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test(self):
        self.assertEqual(max_integer([5, -15843, 7, 9456, 752]), 9456)
        self.assertEqual(max_integer([0, -15843, 7, 9456, 752]), 9456)
        self.assertEqual(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer((1, 67, 3, 5))
        with self.assertRaises(TypeError):
            max_integer('Holberton')
