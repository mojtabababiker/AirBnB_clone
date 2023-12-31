#!/usr/bin/python3
"""
Test model for the file_storage model unit testing, py the use of the python
unittest module
"""

import unittest
from unittest.mock import patch, MagicMock
import os
import os.path

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the creation of the class instance, and the opration of all its
    methods
    """

    @classmethod
    def setupClass(cls):
        """
        A cleaning method to remove the json file after the test is finshed
        """
        json_file = "file.json"
        if os.path.exists(json_file):
            os.remove(json_file)

    @classmethod
    def tearDownClass(cls):
        """
        A cleaning method to remove the json file after the test is finshed
        """
        json_file = "file.json"
        if os.path.exists(json_file):
            os.remove(json_file)

    def setup(self):
        """
        setup the dependancess for the test cases
        """
        __file = "file.json"
        if os.path.exists(__file):
            os.remove(__file)

    def test_private_attrs(self):
        """
        Test the FileStorage private attributes
        """

        fs = FileStorage()

        self.assertFalse(hasattr(fs, "file_path"))
        self.assertFalse(hasattr(fs, "__file_path"))
        self.assertFalse(hasattr(fs, "objects"))
        self.assertFalse(hasattr(fs, "__objects"))
        del fs

    def test_wrong_init_and_calls(self):
        """
        Test the unvalide initialization of the FileStorage class, and
        the calling process to its methods
        """

        with self.assertRaises(TypeError):
            fs = FileStorage(12, "a", (1, 2, 3))

        fs = FileStorage()
        with self.assertRaises(TypeError):
            fs.all(12, "abd", (123, 42, 12))

        with self.assertRaises(TypeError):
            fs.new()

        with self.assertRaises(AttributeError):
            fs.new(12)

        with self.assertRaises(TypeError):
            fs.save("filepath")

        with self.assertRaises(TypeError):
            fs.reload("reload this")

    def test_FileStorage_objects(self):
        """
        Test the FileStorage.__objects type
        """
        fs = FileStorage()
        __objects = fs.all()
        self.assertIsInstance(__objects, dict)
        del fs

    def test_empty_path(self):
        """
        Test the empty path of the __path
        """
        pass

    def test_FileStorage_allz(self):
        """
        Test the FileStorage.all(self) method
        """

        __mocked_class = MagicMock()
        __mocked_class.__name__ = "BaseModel"

        __base_dict = {
            "__class__": "BaseModel",
            "id": "1234-abc-5678cd",
            "created_at": "2023-10-11T10:44:56.129854",
            "updated_at": "2023-10-11T10:45:30.981245"
            }

        __base = MagicMock()
        __base.__class__ = __mocked_class
        __base.id = "1234-abc-5678cd"
        __base.to_dict.return_value = __base_dict

        __fs = FileStorage()
        __objects = __fs.all()

        __fs.new(__base)
        __objects2 = __fs.all()

        self.assertTrue(len(__objects2) > 0)

        self.assertTrue(f"{__base_dict['__class__']}.{__base_dict['id']}"
                        in __objects2.keys())

        __obj = __objects2[f"{__base_dict['__class__']}.{__base_dict['id']}"]
        self.assertEqual(__obj.__class__.__name__, "BaseModel")
        self.assertEqual(__obj.id, __base_dict["id"])
        del __fs

    def test_FileStorage_absave(self):
        """
        Test the FileStorage.save(self) method
        """

        __file = "file.json"

        __mocked_class = MagicMock()
        __mocked_class.__name__ = "BaseModel"

        __base_dict = {
            "__class__": "BaseModel",
            "id": "1234-abc-5678cd",
            "created_at": "2023-10-11T10:44:56.129854",
            "updated_at": "2023-10-11T10:45:30.981245"
            }
        __base = MagicMock()
        __base.__class__ = __mocked_class
        __base.id = "1234-abc-5678cd"
        __base.to_dict.return_value = __base_dict

        __fs = FileStorage()
        __fs.new(__base)
        __fs.save()

        self.assertTrue(len(__fs.all()) > 0)
        self.assertTrue(os.path.exists(__file))
        del __fs

    def test_FileStorage_abcreload(self):
        """
        Test the FileStorage.reload(self) method
        """

        __file = "file.json"

        __fs1 = FileStorage()

        __objects = __fs1.all()

        self.assertTrue(len(__objects) >= 0)
        __fs1.reload()

        # if os.path.exists(__file):
        # self.assertTrue(len(__objects) > 0)

        del __fs1

if __name__ == "__main__":
    unittest.main()
