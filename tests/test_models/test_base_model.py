#!/usr/bin/python3
"""Unit test for BaseModel."""

import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from unittest.mock import patch
from io import StringIO
import sys


class BaseModelTestCase(unittest.TestCase):
    """Class for testing BaseModel."""

    def setUp(self):
        """Set up test environment."""
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, mode='w', encoding='utf_8') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        """Clean up after tests."""
        sys.stdout = sys.__stdout__

    def test_init_attributes(self):
        """Test initialization attributes."""
        bm = BaseModel()

        self.assertTrue(hasattr(bm, "__init__"))
        self.assertTrue(hasattr(bm, "__str__"))
        self.assertTrue(hasattr(bm, "save"))
        self.assertTrue(hasattr(bm, "to_dict"))

        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))

        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

        self.assertRegex(bm.id,
                         r'^[0-9a-f]{8}-[0-9a-f]{4}-'
                         r'[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                         r'[0-9a-f]{12}$')

    def test_attributes_update(self):
        """Test attributes update."""
        bm = BaseModel()
        bmKey = "BaseModel." + bm.id

        bm.name = "My First Model"
        bm.my_number = 89

        self.assertTrue(hasattr(bm, "name"))
        self.assertTrue(hasattr(bm, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[bmKey], "name"))
        self.assertTrue(hasattr(models.storage.all()[bmKey], "my_number"))

    def test_save_method(self):
        """Test save method."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)
        self.assertGreater(bm.updated_at, old_updated_at)

    def test_save_calls_storage_save(self):
        """Test if save() calls models.storage.save()."""
        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

    def test_save_json_file(self):
        """Test if data is saved to JSON file."""
        bm = BaseModel()
        bmKey = "BaseModel." + bm.id
        bm.save()

        with open(self.filepath, mode='r', encoding='utf_8') as file:
            data = json.load(file)

        self.assertIn(bmKey, data)
        self.assertEqual(data[bmKey], bm.to_dict())

    def test_init_from_dict(self):
        """Test initializing from dictionary."""
        bm = BaseModel()
        bm.name = "John"
        bm.my_number = 89

        bm2 = BaseModel(**bm.to_dict())

        self.assertEqual(bm.id, bm2.id)
        self.assertEqual(bm.name, "John")
        self.assertEqual(bm.my_number, 89)
        self.assertEqual(bm.to_dict(), bm2.to_dict())

    def test_init_from_dict_different_instance(self):
        """Test initializing from dictionary creates a different instance."""
        bm = BaseModel()
        bm2 = BaseModel(bm.to_dict())

        self.assertNotEqual(bm, bm2)
        self.assertNotEqual(bm.id, bm2.id)
        self.assertTrue(isinstance(bm2.created_at, datetime))
        self.assertTrue(isinstance(bm2.updated_at, datetime))

    def test_to_string_representation(self):
        """Test __str__ representation."""
        bm = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_str)

    def test_updated_at_after_save(self):
        """Test if updated_at changes after save()."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertGreater(bm.updated_at, old_updated_at)


if __name__ == '__main__':
    unittest.main()
