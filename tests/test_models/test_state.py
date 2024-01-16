#!/usr/bin/python3
""" unit test for State """
import unittest
from models.state import State
from datetime import datetime


class StateTestCase(unittest.TestCase):
    """ class for State test """

    def test_state(self):
        """Check Attributes existence."""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))

        """Check Attributes type"""
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
