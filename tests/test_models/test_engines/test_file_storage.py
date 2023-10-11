#!/usr/bin/env python3
"""
Test model for the file_storage model unit testing, py the use of the python
unittest module
"""

import unittest
from unittest.mock import patch, MagicMock
import os.path

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the creation of the class instance, and the opration of all its
    methods
    """

    def test_private_attrs(self):
        """
        Test the FileStorage private attributes
        """

        fs = FileStorage()

        self.assertFalse(hasattr(fs, file_path))
        self.assertFalse(hasattr(fs, __file_path))
        self.assertFalse(hasattr(fs, objects))
        self.assertFalse(hasattr(fs, __objects))

    def test_wrong_init_and_calls(self):
        """
        Test the unvalide initialization of the FileStorage class, and
        the calling process to its methods
        """

        with self.assertRaises(TypeError):
            fs = FileStorge(12, "a", (1, 2, 3))

        fs = FileStorage()
        with self.assertRaises(TypeError):
            fs.all(12, "abd", (123,42,12))
        with self.assertRaises(TypeError):
            fs.new()

        with self.assertRaises(AttributeError)):
            fs.new(12)

        with self.assertRaises(TypeError):
            fs.save("filepath")

        with self.assertRaises(TypeError):
            fs.reload("reload this")

    def test_file_storage_all(self):
        """
        Test the FileStorage.all(self) method
        """

        __base_dict = {
            "__class__": "BaseModel",
            "id": "1234-abc-5678cd",
            "created_at": "2023-10-11T10:44:56.129854",
            "updated_at": "2023-10-11T10:45:30.981245"
            }
        __base = MagicMock()
        __base.to_dict.return_value = __base_dict

        __fs = Filestorage()
        __objects = __fs.all()

        self.assertTrue(len(__objects) == 0)

        __fs.new(__base)
        __objects2 = __fs.all()

        self.assertTrue(len(__objects2) == 1)
        self.assertTrue(f"BaseModel.{__base.id}" in __objects2.keys())

        __obj = __objects2[f"BaseModel.{__base.id}"]
        self.assertEqual(__obj["__class__"], "BaseModel")
        self.assertEqual(__obj["created_at"], __base_dict["created_at"])
        self.assertEqual(__obj["updated_at"], __base_dict["updated_at"])
        self.assertEqual(__obj["id"], __base_dict["id"])

    def test_FileStorage_save(self):
        """
        Test the FileStorage.save(self) method
        """
        __file = "models/engine/file.json"

        __base_dict = {
            "__class__": "BaseModel",
            "id": "1234-abc-5678cd",
            "created_at": "2023-10-11T10:44:56.129854",
            "updated_at": "2023-10-11T10:45:30.981245"
            }
        __base = MagicMock()
        __base.to_dict.return_value = __base_dict
        with sefl.assertRiases(FileNotFoundError):
            open(__file)
        self.assertFalse(os.path.exists(__file))

        __fs.new(__base)
        __fs.save()

        self.assertTrue(os.path.exists(__file))

    def test_FileStorage_save_reload(self):
        """
        Test the FileStorage.reload(self) method
        """
        __file = "models/engine/file.json"
        __fs = FileStorage()

        __fs.reload()

        __objects = __fs.all()

        if os.path.exists(__file):
            self.assertTrue(len(__objects) > 0)

        else:
            self.assertTrue(len(__objects) == 0)

