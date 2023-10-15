#!/usr/bin/python3
"""
Test module for Review Class
"""
from models.review import Review
from datetime import datetime
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
    
    def test_user_stored(self):
        """ tests review instance storged in storage"""
        self.assertIn(Review(), models.storage.all().values())

    def test_unique_reviews(self):
        """ tests Review instances have unique id"""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_None_arg(self):
        """ pass None as arguments"""
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_attr(self):
        """Test Review instances have attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_Review_to_dict(self):
        """Test the dictionery of a Review instance"""
        time = datetime.today()
        review = Review()
        review.id = "1234-753223-18"
        review.place_id = "5689-225566"
        review.user_id = "234567"
        review.text = "nice but small"
        review.created_at = review.updated_at = time
        review_dict = {
            'id': '1234-753223-18',
            'place_id': '5689-225566',
            'user_id': '234567',
            'text': 'nice but small',
            '__class__': 'Review',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(review.to_dict(), review_dict)

    def test_file_update(self):
        """ tests update of file with instance"""
        review = Review()
        review.save()
        review_id = "Review." + review.id
        with open("models/engine/file.json", "r") as file:
            self.assertIn(review_id, file.read())

    def test_dict(self):
        """ test dictionery of instance"""
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def test_None_kwargs(self):
        """ Test passes None as kwargs"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
