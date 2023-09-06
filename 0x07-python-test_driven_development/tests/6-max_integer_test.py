#!/usr/bin/python3
""" unitest for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unitest for max integer"""

    def integer_list(self):
        list1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list1), 4)

    def empty_list(self):
        list2 = []
        self.assertEqual(max_integer(list2), None)

    def float_list(self):
        list3 = [2.2, 3.4, 10.5, 0]
        self.assertEqual(max_integer(list3), 10.5)
