#!/usr/bin/python3
"""Unit test for FileStorage."""

from datetime import datetime
import unittest
from models.base_model import BaseModel
import models
import json
import os


class FileStorageTestCase(unittest.TestCase):
    """ class for base test """
    def setUp(self):
        self.filepath = models.storage._FileStorage__file_path
        # Create an empty file for testing
        open(self.filepath, 'w').close()
        self.objects = models.storage._FileStorage__objects

    def tearDown(self):
        # Remove the file after tests
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
        self.objects.clear()

    def test_FileStorage_initialisation(self):
        """Check class Attributes."""

        self.assertEqual(self.filepath, "file.json")
        self.assertIsInstance(self.filepath, str)
        self.assertIsInstance(self.objects, dict)
        """Check Existens of BaseModel Methods."""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "__init__"))
        self.assertTrue(hasattr(bm, "__str__"))
        self.assertTrue(hasattr(bm, "save"))
        self.assertTrue(hasattr(bm, "to_dict"))
        """Test if Id is Valid UUID"""
        self.assertTrue(bm.id)
        self.assertIsInstance(bm.id, str)
        self.assertRegex(bm.id,
                         r'^[0-9a-f]{8}-[0-9a-f]{4}-'
                         r'[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                         r'[0-9a-f]{12}$')
        """Test if created_at and updated_at are instances of datetime"""
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_FileStorage_all(self):
        """Check Method all"""
        self.assertIsInstance(models.storage.all(), dict)
        self.assertNotEqual(models.storage.all(), {})

    def test_FileStorage_new(self):
        """Check Method new"""
        bm = BaseModel()
        bmKey = "BaseModel."+bm.id
        self.assertIsInstance(models.storage.all()[bmKey], BaseModel)
        self.assertEqual(models.storage.all()[bmKey], bm)
        self.assertTrue(models.storage.all()[bmKey] is bm)
        self.assertIn(bmKey, models.storage.all())

    def test_FileStorage_save(self):
        """Check Method save"""
        bm = BaseModel()
        bmKey = "BaseModel."+bm.id
        models.storage.save()
        with open(self.filepath, mode='r', encoding='utf_8') as file:
            data = json.load(file)
        self.assertIn(bmKey, data)
        self.assertEqual(data[bmKey], bm.to_dict())

    def test_FileStorage_reload(self):
        """Check Method reload"""
        bm = BaseModel()
        bmKey = "BaseModel." + bm.id
        models.storage.save()
        models.storage.reload()
        self.assertIn(bmKey, models.storage.all())
        self.assertEqual(models.storage.all()[bmKey].id, bm.id)

    def test_FileStorage_file(self):
        """Check file existence"""
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
        self.assertFalse(os.path.exists(self.filepath))
        models.storage.reload()


if __name__ == '__main__':
    unittest.main()
