#!/usr/bin/python3
"""Unittests for Base class"""

import unittest
from models.base import Base
import os


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_id(self):
        """Test the creation of a new Base instance."""
        Base._Base__nb_objects = 0
        base = Base()
        self.assertEqual(base.id, 1)

    def test_make_a_base(self):
        """Check if the IDs are sequential"""
        baseA = Base()
        baseB = Base()
        self.assertEqual(baseA.id, baseB.id - 1)

    def test_assign_id(self):
        """Test if we can assign an ID ourselves."""
        self.assertEqual(98, Base(98).id)

    def test_create_base_with_default_id(self):
        """Test the creation of a new Base with a default id"""
        self.assertIsNotNone(Base()) 
