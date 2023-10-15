#!/usr/bin/python3
"""
Test module for City Class
"""
from models.city import City
from datetime import datetime
import models
import unittest


class TestAmenity(unittest.TestCase):
    """Class for testing instantiation of the City class."""

    def test_doc(self):
        """documentation for the class"""
        doc = City.__doc__
        self.assertIsNotNone(doc)

    def Test_isnstances(self):
        """testing for class instances"""
        city = City()
        self.assertIsInstance(City, City)

    def test_type_attribute(self):
        """tests type of class  attributes"""
        self.assertEqual(str, type(City.name))
        self.assertEqual(str, type(City.State.id))

    def test_city_stored(self):
        """ tests city instance storged in storage"""
        self.assertIn(City(), models.storage.all().values())

    def test_None_arg(self):
        """ pass None as arguments"""
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_attr(self):
        """Test city instances have attributes"""
        city = City()
        self.assertTrue(hasattr(City, "name"))
        self.assertTrue(hasattr(City, "State.id"))

    def test_city_to_dict(self):
        """Test the dictionery of a city instance"""
        time = datetime.today()
        city = City()
        city.name = "Newyork"
        city.id = "122-234"
        city.state.id = "122-23455"
        city.created_at = city.updated_at = time
        city_dict = {
            'name': 'Newyork',
            'id': '122-234',
            'state.id': '122-23455',
            '__class__': 'City',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(city.to_dict(), city_dict)

    def test_unique_city(self):
        """ tests City instances have unique id"""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_file_update(self):
        """ tests update of file with instance"""
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("file.json", "r") as file:
            self.assertIn(city_id, file.read())

    def test_dict(self):
        """ test dictionery of instance"""
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_None_kwargs(self):
        """ Test passes None as kwargs"""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

if __name__ == "__main__":
    unittest.main()
