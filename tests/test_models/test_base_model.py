#!/usr/bin/env python3
"""
This a test module for the BaseModel class from models.base_model
"""

import unittest
from unittest.mock import patch, MagicMock
from models.base_model import BaseModel
from models.base_model import uuid4
from models.base_model import datetime
from models.base_model import storage


class TestBase(unittest.TestCase):
    """
    A test class for the BaseModel class, using the TestCase from unittest
    as a super class
    This Test unit test several cases, such as:
        1] Instances Creation from the BaseModel
        2] Methods of the BaseModel
    """

    def test_creation(self):
        """
        Test the instance initialization, and attributes creation
        """
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    @patch("models.base_model.uuid4")
    def test_id_creation(self, mocked_uuid4):
        """
        Test the base.id attribute value creation
        """
        mocked_uuid4.return_value = 12345
        base = BaseModel()
        self.assertEqual(base.id, str(12345))

    @patch("models.base_model.datetime")
    def test_created_at_and_updated_at_creation(self, mocked_today):
        """
        Test the base.created_at and updated_at attributes creations
        """

        with patch("models.base_model.storage") as mocked_storage:
            # date = MagicMock()
            date_form = "2023-10-11 03:30:45.164253"
            mocked_today.today.return_value = date_form
            # date.isoformat.return_value = date_form
            base = BaseModel()
            self.assertEqual(base.created_at, date_form)
            self.assertEqual(base.updated_at, date_form)

    def test_str(self):
        """
        Test the __str__ method from the BaseModel
        """
        base = BaseModel()

        base_str = f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(str(base), base_str)

    @patch("models.base_model.datetime")
    def test_base_save(self, mocked_today):
        """
        Test the BaseModel.save(self) method
        """
        # date = MagicMock()
        with patch("models.base_model.storage") as mocked_storage:

            mocked_storage.new.return_value = None
            date_form = "2023-10-11 03:43:25.164253"
            mocked_today.today.return_value = date_form
            # date.isoformat.return_value = date_form
            base = BaseModel()
            date_form = "2023-10-11 03:46:45.164253"
            mocked_today.today.return_value = date_form
            # date.isoformat.return_value = date_form
            base.save()
            self.assertEqual(base.updated_at, date_form)
            self.assertNotEqual(base.updated_at, base.created_at)

            with self.assertRaises(TypeError):
                base.save("extra args")

    def test_base_to_dict(self):
        """
        Test the BaseModel.to_dict(self) method
        """

        base = BaseModel()
        base_dict = base.to_dict()
        dict_values = base_dict.values()

        self.assertTrue(base.__class__.__name__ in dict_values)
        self.assertTrue(base.id in dict_values)
        self.assertTrue("updated_at" in base_dict.keys())
        self.assertTrue("created_at" in base_dict.keys())

        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['id'], str)

        isoform = r"\d\d\d\d-\d\d-\d\dT\d+:\d+:\d+.\d+"
        self.assertRegex(base_dict['updated_at'], isoform)
        self.assertRegex(base_dict['created_at'], isoform)

        with self.assertRaises(TypeError):
            base.to_dict(dict_values)

        base.new_attr = "New Attribute"
        base_dict = base.to_dict()
        dict_values = base_dict.values()

        self.assertTrue(base.new_attr in dict_values)

    def test_BaseModel_from_dict(self):
        """
        Test the creation of a BaseModel instance from a dictionery
        """

        instance_dict = {
            "__class__": "BaseModel",
            "id": "1234-753223-18932",
            "created_at": "2023-10-11T05:03:54.743342",
            "updated_at": "2023-10-21T05:03:54.743342"
            }
        base = BaseModel(**instance_dict)

        self.assertEqual(base.__class__.__name__, "BaseModel")
        self.assertEqual(str(base.id), instance_dict["id"])

        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    @patch("models.base_model.storage")
    def test_BaseModel_storage_new(self, mocked_storage):
        """
        Test the storage.new(obj) called by value
        """

        base = BaseModel()
        mocked_storage.new.assert_called_with(base)

    @patch("models.base_model.storage")
    def test_BaseModel_storage_save(self, mocked_storage):
        """
        Test the storage.save() calling
        """
        instance_dict = {
            "__class__": "BaseModel",
            "id": "1234-753223-18932",
            "created_at": "2023-10-11T05:03:54.743342",
            "updated_at": "2023-10-21T05:03:54.743342"
            }
        base = BaseModel(**instance_dict)
        base.save()
        
        self.assertTrue(mocked_storage.save.called)


if __name__ == "__main__":
    unittest.main()
