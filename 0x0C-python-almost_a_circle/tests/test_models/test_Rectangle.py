#!/usr/bin/python3
"""This is  a unittest for class rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle(self):
        rect = Rectangle(4, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_rectangle_with_coord(self):
        rect = Rectangle(9, 6, 3, 1)
        self.assertEqual(rect.width, 9)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 1)

    def test_rect_with_noargs(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-8, 3)

        with self.assertRaises(TypeError):
            rect = Rectangle(7, "4")
