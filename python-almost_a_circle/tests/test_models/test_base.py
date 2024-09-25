#!/usr/bin/python3
"""Unittests for Base class"""

import unittest
from models.base import Base
import os

class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_auto_id_assignment(self):
        """Test if Base() auto assigns ID"""
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)
        self.assertEqual(b4.id, 3)

if __name__ == '__main__':
    unittest.main()
