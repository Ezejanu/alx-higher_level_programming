#!/usr/bin/python3

"""Unittest for max_integer([...])
"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([....])"""

    def is_empty_list(self):
        """ Test for if list is empty"""
        testList = [7]
        self.assertEqual(max_integer(testList), None)

    def list_contains_one_element(self):
        """Testing a list which contains a single element"""
        testList = [4]
        self.assertEqual(max_integer(testList), 4)

    def list_contains_multiple_elements(self):
        """Testing a list which contains multiple elements"""
        testList = [1, 54, 2, 19, 45]
        self.assertEqual(max_integer(testList), 54)

    def max_element_at_beginning(self):
        """Testing a list with max value at the beginning"""
        testList = [102, 54, 2, 19, 45]
        self.assertEqual(max_integer(testList), 102)

    def maz_element_at_end(self):
        """Testing a list which contains multiple elements"""
        testList = [102, 54, 2, 19, 450]
        self.assertEqual(max_integer(testList), 450)

    def list_contains_negative_integers(self):
        """Testing a list which contains multiple elements"""
        testList = [1, 54, -2, 19, -600, 45, 0]
        self.assertEqual(max_integer(testList), 54)

    def list_contains_multiple_elements(self):
        """Testing a list which contains multiple elements"""
        testList = [1, 54, 2, 19, 45]
        self.assertEqual(max_integer(testList), 54)

    if __name__ == "__main__":
        import doctest

        doctest.testmod()
