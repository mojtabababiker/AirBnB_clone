#!/usr/bin/python3
"""
Test module for Review Class
"""
from models.review import Review
from datetime import datetime
import json
import models
import unittest


class TestReview(unittest.TestCase):
    """Class for testing instantiation of the Review class."""

    def test_doc(self):
        """... documentation for the class"""
        doc = Review.__doc__
        self.assertIsNotNone(doc)

    def Test_isnstances(self):
        """testing for class instances"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_type_attribute(self):
        """tests type of class  attributes"""
        self.assertEqual(str, type(Review.place_id))
        self.assertEqual(str, type(Review.user_id))
        self.assertEqual(str, type(Review.text))

    def test_review_stored(self):
        """ tests review instance storged in storage"""
        self.assertIn(Review(), models.storage.all().values())

    def test_unique_reviews(self):
        """ tests Review instances have unique id"""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_None_arg(self):
        """ pass None as arguments"""
        review3 = Review(None)
        self.assertNotIn(None, review3.__dict__.values())

    def test_attr(self):
        """Test Review instances have attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_Review_to_dict(self):
        """Test the dictionery of a Review instance"""
        time = datetime.today()
        review = Review()
        review.id = "1234-753223-18932"
        review.place_id = "321-765432-1234"
        review.user_id = "721-765432-1234"
        review.created_at = review.updated_at = time
        review_dict = {
            'id': '1234-753223-18932',
            '__class__': 'Review',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat(),
            'place_id': "321-765432-1234",
            'user_id': "721-765432-1234"
        }

        self.assertDictEqual(review.to_dict(), review_dict)

    def test_file_update(self):
        """ tests update of file with instance"""
        review = Review()
        review.save()
        review_id = "Review." + review.id
        with open(r"models/engine/file.json", "r") as file:
            self.assertIn(review_id, file.read())

    def test_dict(self):
        """ test dictionery of instance"""
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)


if __name__ == "__main__":
    unittest.main()
