#!/usr/bin/python3
"""Test module tests the ``State`` class, using unittesting"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """Test class for unittests.
    It inherits from unittest's ``TestCase``

    A ``State`` instance will hereafter
    be simply referred to as an "instance"
    """

    def test_instance(self):
        """Checks that an instance is created properly"""
        s1 = State()
        s2 = State()
        self.assertTrue(isinstance(s1, State))
        self.assertTrue(isinstance(s2, State))
        self.assertTrue(type(s1) == State)
        self.assertFalse(type(s2) != State)
        self.assertFalse(isinstance(s1, int))
        self.assertFalse(isinstance(s2, list))
        self.assertFalse(s1 is s2)

    def test_inheritance(self):
        """Checks that an instance inherits from the ``BaseModel`` class"""
        s1 = State()
        s2 = State()
        self.assertTrue(isinstance(s1, BaseModel))
        self.assertTrue(isinstance(s2, BaseModel))
        self.assertFalse(isinstance(s1, int))
        self.assertFalse(isinstance(s2, list))
        self.assertEqual(len(s2.id), 36)
        self.assertFalse(type(s2) == BaseModel)
        self.assertFalse(type(s1) == BaseModel)
        self.assertTrue(type(s1.created_at) == datetime)
        self.assertTrue(type(s2.updated_at) == datetime)

    def test_attributes(self):
        """Checks that an instance has the correct and complete attributes"""
        s1 = State()
        s2 = State()
        a_attr = getattr(s1, "name")
        self.assertTrue(a_attr == "")
        s1.name = "Lagos"
        self.assertEqual(s1.name, "Lagos")
        self.assertTrue(type(s1.name) == str)

        self.assertTrue(s2.id)
        self.assertEqual(len(s1.id), 36)
        self.assertFalse(s2.id == s1.id)

        self.assertTrue(s1.created_at)
        self.assertTrue(type(s1.created_at) == datetime)
        self.assertFalse(s1.created_at == s2.created_at)

        self.assertTrue(s1.updated_at)
        self.assertTrue(type(s1.updated_at) == datetime)
        self.assertFalse(s1.updated_at == s2.updated_at)

        self.assertTrue(s2.name == "")
        self.assertFalse(s1.name == "")

        a_attr = getattr(s2, "__class__")
        self.assertFalse(a_attr == 'State')
        self.assertNotEqual(a_attr, "State")


if __name__ == '__main__':
    unittest.main()
