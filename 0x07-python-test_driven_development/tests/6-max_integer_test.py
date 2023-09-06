#!/usr/bin/python3
""" unitest for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unitest for max integer"""

    def test_list(self):
        list1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list1), 4)
