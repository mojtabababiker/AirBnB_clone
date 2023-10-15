#!/usr/bin/python3
"""
Test module for Place Class
"""
from models.place import Place
from datetime import datetime
import models
import unittest


class TestPlace(unittest.TestCase):
    """Class for testing instantiation of the Place class."""

    def test_doc(self):
        """Test documentation for the class"""
        doc = Place.__doc__
        self.assertIsNotNone(doc)

    def Test_isnstances(self):
        """testing for class instances"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_type_attribute(self):
        """tests type of class  attributes"""
        self.assertEqual(str, type(Place.city_id))
        self.assertEqual(str, type(Place.user_id))
        self.assertEqual(str, type(Place.name))
        self.assertEqual(str, type(Place.description))
        self.assertEqual(int, type(Place.number_rooms))
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertEqual(int, type(Place.max_guest))
        self.assertEqual(int, type(Place.price_by_night))
        self.assertEqual(float, type(Place.latitude))
        self.assertEqual(float, type(Place.longitude))
        self.assertEqual(list, type(Place.amenity_ids))
    
    def test_place_stored(self):
        """ tests place instance storged in storage"""
        self.assertIn(Place(), models.storage.all().values())

    def test_unique_places(self):
        """ tests Place instances have unique id"""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_None_arg(self):
        """ pass None as arguments"""
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_attr(self):
        """Test Place instances have attributes"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_Place_to_dict(self):
        """Test the dictionery of a Place instance"""
        time = datetime.today()
        place = Place()
        place.id = "1234-753223-18932"
        place.city_id = "1234-753223"
        place.user_id = "1234-753223-1888"
        place.name = " Bear home"
        place.number_rooms = 3
        place.price_by_night = 300
        place.created_at = place.updated_at = time
        place_dict = {
            'id': '1234-753223-18932',
            'city_id': '1234-753223',
            'user_id': '1234-753223-1888',
            'name': 'Bear home',
            'number_rooms': 3,
            'price_by_night': 300,
            '__class__': 'Place',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(place.to_dict(), place_dict)

    def test_file_update(self):
        """ tests update of file with instance"""
        place = Place()
        place.save()
        place_id = "Place." + place.id
        with open("file.json", "r") as file:
            self.assertIn(place_id, file.read())

    def test_dict(self):
        """ test dictionery of instance"""
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)
    
    def test_None_kwargs(self):
        """ Test passes None as kwargs"""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
