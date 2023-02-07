#!/usr/bin/python3
"""Test module tests the ``BaseModel`` package, using unittesting"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBase(unittest.TestCase):
    """Test class for unittests.
    It inherits from unittest's ``TestCase``

    A ``BaseModel`` instance will hereafter
    be simply referred to as "instance"
    """

    def test_instance(self):
        """Check that an instance is created properly"""

        base1 = BaseModel()
        base2 = BaseModel()
        base3 = BaseModel()
        self.assertTrue(isinstance(base1, BaseModel))
        self.assertTrue(isinstance(base2, BaseModel))
        self.assertTrue(isinstance(base3, BaseModel))
        self.assertFalse(isinstance(base1, int))
        self.assertFalse(isinstance(base2, str))
        self.assertFalse(isinstance(base3, list))

    def test_attributes(self):
        """Check that an instance
        correctly initializes its instance attributes
        """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertTrue(isinstance(base1.created_at, datetime))
        self.assertTrue(isinstance(base2.created_at, datetime))
        self.assertTrue(isinstance(base1.updated_at, datetime))
        self.assertTrue(isinstance(base2.updated_at, datetime))
        self.assertTrue(base1.id)
        self.assertTrue(base2.id)
        self.assertEqual(len(base1.id), 36)
        self.assertEqual(len(base2.id), 36)
        self.assertNotEqual(len(base1.id), 20)
        self.assertNotEqual(len(base2.id), 20)
        self.assertTrue(isinstance(base1.id, str))
        self.assertTrue(isinstance(base2.id, str))
        self.assertFalse(isinstance(base1.id, tuple))
        self.assertFalse(isinstance(base1.id, list))



