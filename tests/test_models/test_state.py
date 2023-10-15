#!/usr/bin/python3
"""
Test module for State Class
"""
from models.state import State
from datetime import datetime
import models
import unittest


class TestState(unittest.TestCase):
    """Class for testing instantiation of the State class."""

    def test_doc(self):
        """... documentation for the class"""
        doc = State.__doc__
        self.assertIsNotNone(doc)

    def Test_isnstances(self):
        """testing for class instances"""
        state = State()
        self.assertIsInstance(state, State)

    def test_type_attribute(self):
        """tests type of class  attributes"""
        self.assertEqual(str, type(State.name))

    def test_state_stored(self):
        """ tests State instance storged in storage"""
        self.assertIn(State(), models.storage.all().values())

    def test_unique_states(self):
        """ tests State instances have unique id"""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_None_arg(self):
        """ pass None as arguments"""
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_attr(self):
        """Test State instances have attributes"""
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_State_to_dict(self):
        """Test the dictionery of a State instance"""
        time = datetime.today()
        state = State()
        state.id = "753223-18932"
        state.name = "New York"
        state.created_at = state.updated_at = time
        state_dict = {
            'name': 'New York',
            'id': '753223-18932',
            '__class__': 'State',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(state.to_dict(), state_dict)

    def test_file_update(self):
        """ tests update of file with instance"""
        state = State()
        state.save()
        state_id = "State." + state.id
        with open("models/engine/file.json", "r") as file:
            self.assertIn(state_id, file.read())

    def test_dict(self):
        """ test dictionery of instance"""
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_None_kwargs(self):
        """ Test passes None as kwargs"""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
