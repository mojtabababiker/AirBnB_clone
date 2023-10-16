#!/usr/bin/python3
"""
Test module for User Class
"""
from models.user import User
from datetime import datetime
import json
import models
import unittest


class TestUser(unittest.TestCase):
    """Class for testing instantiation of the User class."""

    def test_doc(self):
        """test the documentation for the class"""
        doc = User.__doc__
        self.assertIsNotNone(doc)

    def Test_isnstances(self):
        """testing for class instances"""
        user = User()
        self.assertIsInstance(user, User)

    def test_type_attribute(self):
        """tests type of class  attributes"""
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))

    def test_user_stored(self):
        """ tests user instance storged in storage"""
        self.assertIn(User(), models.storage.all().values())

    def test_unique_users(self):
        """ tests User instances have unique id"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_None_arg(self):
        """ pass None as arguments"""
        user3 = User(None)
        self.assertNotIn(None, user3.__dict__.values())

    def test_attr(self):
        """Test User instances have attributes"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_User_to_dict(self):
        """Test the dictionery of a User instance"""
        time = datetime.today()
        user = User()
        user.id = "1234-753223-18932"
        user.email = "jisook@gmail.com"
        user.password = "105A$55"
        user.first_name = "jisook"
        user.last_name = "kang"
        user.created_at = user.updated_at = time
        user_dict = {
            'email': 'jisook@gmail.com',
            'password': '105A$55',
            'first_name': 'jisook',
            'last_name': 'kang',
            'id': '1234-753223-18932',
            '__class__': 'User',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }

        self.assertDictEqual(user.to_dict(), user_dict)

    def test_file_update(self):
        """ tests update of file with instance"""
        user = User()
        user.save()
        user_id = "User." + user.id
        with open(r"file.json", "r") as file:
            self.assertIn(user_id, file.read())

    def test_dict(self):
        """ test dictionery of instance"""
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)


if __name__ == "__main__":
    unittest.main()
