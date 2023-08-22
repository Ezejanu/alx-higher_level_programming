#!/usr/bin/python3
"""This is a unittest for parent class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_with_id(self):
        obj = Base(8)
        self.assertEqual(obj.id, 8)

    def test_base_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_base_without_id_2(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_base_with_negative_id(self):
        obj = Base(-3)
        self.assertEqual(obj.id, -3)

    def test_base_with_zero_id(self):
        obj = Base(0)
        self.assertEqual(obj.id, 0)

    def test_base_with_float_id(self):
        obj = Base(2.67)
        self.assertEqual(obj.id, 2.67)

    def test_base_with_string_id(self):
        obj = Base("idr")
        self.assertEqual(obj.id, "idr")
