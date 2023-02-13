#!/usr/bin/python3
"""The test module for user.py"""
import unittest
import models
import os, shutil
from datetime import datetime as dt
from models.amenity import Amenity



class TestState(unittest.TestCase):

    def setUp(self):
        self.my_state = Amenity()
        self.my_state.name = "Betty"
        self.my_state.save()
        
        self.my_state2 = Amenity()
        self.my_state2.name = "John"
        self.my_state2.save()


    def test_class(self):
        self.assertIsInstance(self.my_state, Amenity)
        self.assertIsInstance(self.my_state2, Amenity)

    def test_id(self):
        self.assertIsInstance(self.my_state.id, str)
        self.assertIsInstance(self.my_state2.id, str)

    def test_stored(self):
        self.assertIn(self.my_state, models.storage.all().values())
        self.assertIn(self.my_state2, models.storage.all().values())

    def test_created_at_type(self):
        self.assertIsInstance(self.my_user.created_at, dt)
        self.assertIsInstance(self.my_user2.created_at, dt)

    def test_updated_at_type(self):
        self.assertIsInstance(self.my_state.updated_at, dt)
        self.assertIsInstance(self.my_state2.updated_at, dt)

    def test_name_type(self):
        self.assertIsInstance(self.my_state.name, str)
        self.assertIsInstance(self.my_state2.name, str

    def test_unique_ids(self):
        self.assertNotEqual(self.my_state, self.my_state2)

    def test_diff_times(self):
        self.assertLess(self.my_state.created_at, self.my_state2.created_at)
        self.assertLess(self.my_state.updated_at, self.my_state2.updated_at)

    def test_instance_params(self):
        self.assertEqual(self.my_state.name, "Betty")
        self.assertEqual(self.my_state2.name, "John")

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            State(created_at=None, updated_at=None)

    def test_to_dict_keys(self):
        the_dict = self.my_state.to_dict()
        self.assertIn("id", the_dict)
        self.assertIn("created_at", the_dict)
        self.assertIn("updated_at", the_dict)
        self.assertIn("__class__", the_dict)
        self.assertIn("name", the_dict)

    def test_compare_to_dict_magic(self):
        self.assertNotEqual(self.my_state.to_dict(), self.my_state.__dict__)
        self.assertNotEqual(self.my_state2.to_dict(), self.my_state2.__dict__)


class TestStateSave(unittest.TestCase):
    """Inside the class"""

    __src = "file.json"
    __dest = "tmp.json"

    def setUp(self):
        self.my_state = Amenity()
        self.upd_at = self.my_state.updated_at
        self.my_state.save()

        if self.__src in os.listdir(os.getcwd()):
            shutil.copy(self.__src, self.__dest)

    def tearDown(self):

        if self.__dest in os.listdir(os.getcwd()):
            os.remove(self.__dest)

    def test_save_works(self):
        self.assertIn(self.__src, os.listdir(os.getcwd()))

    def test_save_updated_at(self):
        self.my_state.save()
        self.assertLess(self.upd_at, self.my_user.updated_at)

    def test_save_args(self):
        with self.assertRaises(TypeError):
            self.my_state.save(None)

    def test_save_kwargs(self):
        with self.assertRaises(TypeError):
            self.my_state.save(obj=None)

if __name__ == '__main__':
    unittest.main()



