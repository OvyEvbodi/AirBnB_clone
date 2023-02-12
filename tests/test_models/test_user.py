#!/usr/bin/python3
"""Test module tests the ``User`` class, using unittesting"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """Test class for unittests.
    It inherits from unittest's ``TestCase``

    A ``User`` instance will hereafter
    be simply referred to as an "instance"
    """

    def setUp(self):
        """Runs before every test method"""
        self.user = User()
        self.user.email = "user@email.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def test_instance(self):
        """Checks that an instance is created properly"""
        user1 = User()
        user2 = User()
        self.assertTrue(isinstance(user1, User))
        self.assertTrue(isinstance(user2, User))
        self.assertTrue(type(user1) == User)
        self.assertFalse(type(user2) != User)
        self.assertFalse(isinstance(user1, int))
        self.assertFalse(isinstance(user2, list))
        self.assertFalse(user1 is user2)

    def test_inheritance(self):
        """Checks that an instance inherits from the ``BaseModel`` class"""
        user1 = User()
        user2 = User()
        self.assertTrue(isinstance(user1, BaseModel))
        self.assertTrue(isinstance(user2, BaseModel))
        self.assertFalse(isinstance(user1, int))
        self.assertFalse(isinstance(user2, list))
        self.assertEqual(len(user2.id), 36)
        self.assertFalse(type(user2) == BaseModel)
        self.assertFalse(type(user1) == BaseModel)
        self.assertTrue(type(user1.created_at) == datetime)
        self.assertTrue(type(user2.updated_at) == datetime)

    def test_attributes(self):
        """Checks that an instance has the correct and complete attributes"""
        user1 = User()
        user2 = User()
        a_attr = getattr(user1, "email")
        self.assertTrue(a_attr == "")
        user1.email = "ovangy@ovy.com"
        self.assertEqual(user1.email, "ovangy@ovy.com")
        self.assertTrue(type(user1.email) == str)

        a_attr = getattr(user1, "password")
        self.assertTrue(a_attr == "")
        user1.password = "donthackme"
        self.assertEqual(user1.password, "donthackme")
        self.assertTrue(type(user1.password) == str)

        a_attr = getattr(user1, "first_name")
        self.assertTrue(a_attr == "")
        user1.first_name = "ovangy"
        self.assertEqual(user1.first_name, "ovangy")
        self.assertTrue(type(user1.first_name) == str)

        a_attr = getattr(user1, "last_name")
        self.assertTrue(a_attr == "")
        user1.last_name = "Zaram"
        self.assertEqual(user1.last_name, "Zaram")
        self.assertTrue(type(user1.last_name) == str)

        self.assertTrue(user2.id)
        self.assertEqual(len(user1.id), 36)
        self.assertFalse(user1.id == user2.id)

        self.assertTrue(user1.created_at)
        self.assertTrue(type(user1.created_at) == datetime)
        self.assertFalse(user1.created_at == user2.created_at)

        self.assertTrue(user1.updated_at)
        self.assertTrue(type(user1.updated_at) == datetime)
        self.assertFalse(user1.updated_at == user2.updated_at)

        self.assertFalse(user1.email == "")
        self.assertFalse(user1.password == "")
        self.assertFalse(user1.first_name == "")
        self.assertFalse(user1.last_name == "")
        self.assertTrue(user2.email == "")
        self.assertTrue(user2.password == "")
        self.assertTrue(user2.first_name == "")
        self.assertTrue(user2.last_name == "")

        a_attr = getattr(user1, "__class__")
        self.assertFalse(a_attr == 'User')
        self.assertNotEqual(a_attr, "User")

    def test_save(self):
        """Test the `save` method"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Test the `to_dict` method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], "user@email.com")
        self.assertEqual(user_dict["password"], "password")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")


if __name__ == '__main__':
    unittest.main()
