#!/usr/bin/python3
"""
Test module for City Class
"""
from models.city import City
from datetime import datetime
import json
import models
import unittest


class TestCity(unittest.TestCase):
    """Class for testing instantiation of the City class."""

    def test_doc(self):
        """... documentation for the class"""
        doc = City.__doc__
        self.assertIsNotNone(doc)

    def Test_isnstances(self):
        """testing for class instances"""
        city = City()
        self.assertIsInstance(city, City)

    def test_type_attribute(self):
        """tests type of class  attributes"""
        self.assertEqual(str, type(City.name))
        self.assertEqual(str, type(City.state_id))

    def test_city_stored(self):
        """ tests city instance storged in storage"""
        self.assertIn(City(), models.storage.all().values())

    def test_unique_citys(self):
        """ tests City instances have unique id"""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_None_arg(self):
        """ pass None as arguments"""
        city3 = City(None)
        self.assertNotIn(None, city3.__dict__.values())

    def test_attr(self):
        """Test City instances have attributes"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_City_to_dict(self):
        """Test the dictionery of a City instance"""
        time = datetime.today()
        city = City()
        city.id = "1234-753223-18932"
        city.name = "jisook"
        city.state_id = "321-765432-1234"
        city.created_at = city.updated_at = time
        city_dict = {
            'id': '1234-753223-18932',
            '__class__': 'City',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat(),
            'name': "jisook",
            'state_id': "321-765432-1234"
        }

        self.assertDictEqual(city.to_dict(), city_dict)

    def test_file_update(self):
        """ tests update of file with instance"""
        city = City()
        city.save()
        city_id = "City." + city.id
        with open(r"models/engine/file.json", "r") as file:
            self.assertIn(city_id, file.read())

    def test_dict(self):
        """ test dictionery of instance"""
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)


if __name__ == "__main__":
    unittest.main()
