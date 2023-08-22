#!/usr/bin/python3
"""This is a unittest for parent class Base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Unittest for class Base)"""
    def test_base_with_id(self):
        obj = Base(8)
        self.assertEqual(obj.id, 8)

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

if __name__ == '__main__':
    unittest.main()
