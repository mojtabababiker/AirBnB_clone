#!/usr/bin/python3
"""
Test module for Amenity Class
"""
from models.amenity import Amenity
from datetime import datetime
import models
import unittest


class TestAmenity(unittest.TestCase):
    """Class for testing instantiation of the Amenity class."""

    def test_doc(self):
        """documentation for the class"""
        doc = Amenity.__doc__
        self.assertIsNotNone(doc)

    def Test_isnstances(self):
        """testing for class instances"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_type_attribute(self):
        """tests type of class  attributes"""
        self.assertEqual(str, type(Amenity.name))

    def test_amenity_stored(self):
        """ tests amenity instance storged in storage"""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_None_arg(self):
        """ pass None as arguments"""
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_attr(self):
        """Test Amenity instances have attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(Amenity, "name"))

    def test_Amenity_to_dict(self):
        """Test the dictionery of a Amenity instance"""
        time = datetime.today()
        amenity = Amenity()
        amenity.name = "Piscina"
        amenity.id = "122234"
        amenity.created_at = amenity.updated_at = time
        amenity_dict = {
            'name': 'Piscina',
            'id': '122234',
            '__class__': 'Amenity',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(amenity.to_dict(), amenity_dict)

    def test_unique_amenitys(self):
        """ tests User instances have unique id"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_file_update(self):
        """ tests update of file with instance"""
        amenity = Amenity()
        amenity.save()
        amenity_id = "Amenity." + amenity.id
        with open("models/engine/file.json", "r") as file:
            self.assertIn(amenity_id, file.read())

    def test_dict(self):
        """ test dictionery of instance"""
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)

    def test_None_kwargs(self):
        """ Test passes None as kwargs"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
