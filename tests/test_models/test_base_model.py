#!/usr/bin/env python3
"""
This a test module for the BaseModel class from models.base_model
"""

import unittest
from models.base_model import BaseModel
from models.base_model import uuid4
from models.base_model import datetime


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
        self.assertTrue(hasattr(base, "updates_at"))

    @unittest.patch("uuid4")
    def test_id_creation(self, mocked_uuid4):
        """
        Test the base.id attribute value creation
        """
        mocked_uuid4.return_value = 12345
        base = BaseModel()
        self.assertEqual(base.id, str(12345))

    @unittest.patch("datetime.today")
    def test_created_at_and_updated_at_creation(self, mocked_today):
        """
        Test the base.created_at and updated_at attributes creations
        """

        date = "2023-10-11T03:30:45.164253"
        mocked_today.return_value = date
        base = BaseModel()
        self.assertEqual(base.created_at, date)
        self.assertEqual(base.updated_at, date)

    def test_str(self):
        """
        Test the __str__ method from the BaseModel
        """
        base = BaseModel()

        base_str = f"[{base.__clase__.__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(str(base), base_str)

    @unittest.patch("datetime.today")
    def test_base_save(self, mocked_today):
        """
        Test the BaseModel.save(self) method
        """
        date = "2023-10-11T03:43:25.164253"
        mocked_today.return_value = date
        base = BaseModel()
        date = "2023-10-11T03:46:45.164253"
        mocked_today.return_value = date
        base.save()
        self.assertEqual(base.updated_at, date)
        self.assertNotEqual(base.updated_at, base.created_at)

        with self.assertRaises("TypeError"):
            base.save("extra args")

    def test_base_to_dict(self):
        """
        Test the BaseModel.to_dict(self) method
        """

        base = BaseModel()
        base_dict = base.to_dict()
        dict_values = base_dict.values()
        self.assertTrue(base.__clase__.__name__ is in dict_values)
        self.assertTrue(str(base.updated_at) is in dict_values)
        self.assertTrue(str(base.created_at) is in dict_values)
        self.assertTrue(base.id is in dict_values)

        with self.assertRiases("TypeError"):
            base.to_dict(dict_values)

        base.new_attr = "New Attribute"
        base_dict = base.to_dict()
        dict_values = base_dict.values()

        self.assertTrue(base.new_attr is in dict_values)

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
        self.assertEqaul(str(base.created_at), instance_dict["created_at"])
        self.assertEqual(str(base.updated_at), instance_dict["updated_at"])


if __name__ == "__main__":
    unittest.main()
