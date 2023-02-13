#!/usr/bin/python3
"""The test module for user.py"""
import unittest
import models
import os, shutil
from datetime import datetime as dt
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.my_user = User()
        self.my_user.first_name = "Betty"
        self.my_user.last_name = "Bar"
        self.my_user.email = "airbnb@mail.com"
        self.my_user.password = "root"
        self.my_user.save()
        
        self.my_user2 = User()
        self.my_user2.first_name = "John"
        self.my_user2.email = "airbnb2@mail.com"
        self.my_user2.password = "root"
        self.my_user2.save()


    def test_class(self):
        self.assertIsInstance(self.my_user, User)
        self.assertIsInstance(self.my_user2, User)

    def test_id(self):
        self.assertIsInstance(self.my_user.id, str)
        self.assertIsInstance(self.my_user2.id, str)

    def test_stored(self):
        self.assertIn(self.my_user, models.storage.all().values())
        self.assertIn(self.my_user2, models.storage.all().values())

    def test_created_at_type(self):
        self.assertIsInstance(self.my_user.created_at, dt)
        self.assertIsInstance(self.my_user2.created_at, dt)

    def test_updated_at_type(self):
        self.assertIsInstance(self.my_user.updated_at, dt)
        self.assertIsInstance(self.my_user2.updated_at, dt)

    def test_email_type(self):
        self.assertIsInstance(self.my_user.email, str)
        self.assertIsInstance(self.my_user2.email, str)

    def test_first_name_type(self):
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertIsInstance(self.my_user2.first_name, str)

    def test_last_name_type(self):
        self.assertIsInstance(self.my_user.last_name, str)
        self.assertIsInstance(self.my_user2.last_name, str)

    def test_password_type(self):
        self.assertIsInstance(self.my_user.password, str)
        self.assertIsInstance(self.my_user2.password, str)

    def test_unique_ids(self):
        self.assertNotEqual(self.my_user, self.my_user2)

    def test_diff_times(self):
        self.assertLess(self.my_user.created_at, self.my_user2.created_at)
        self.assertLess(self.my_user.updated_at, self.my_user2.updated_at)

    def test_instance_params(self):
        self.assertEqual(self.my_user.first_name, "Betty")
        self.assertEqual(self.my_user.last_name, "Bar")
        self.assertEqual(self.my_user.email, "airbnb@mail.com")
        self.assertEqual(self.my_user.password, "root")

        self.assertEqual(self.my_user2.first_name, "John")
        self.assertEqual(self.my_user2.last_name, "")
        self.assertEqual(self.my_user2.email, "airbnb2@mail.com")
        self.assertEqual(self.my_user2.password, "root")

    def test_kwargs_none(self):
        with self.assertRaises(TypeError):
            User(created_at=None, updated_at=None)

    def test_to_dict_keys(self):
        the_dict = self.my_user.to_dict()
        self.assertIn("id", the_dict)
        self.assertIn("created_at", the_dict)
        self.assertIn("updated_at", the_dict)
        self.assertIn("__class__", the_dict)
        self.assertIn("first_name", the_dict)
        self.assertIn("last_name", the_dict)
        self.assertIn("email", the_dict)
        self.assertIn("password", the_dict)

    def test_compare_to_dict_magic(self):
        self.assertNotEqual(self.my_user.to_dict(), self.my_user.__dict__)
        self.assertNotEqual(self.my_user2.to_dict(), self.my_user2.__dict__)


class TestUserSave(unittest.TestCase):
    """Inside the class"""

    __src = "file.json"
    __dest = "tmp.json"

    def setUp(self):
        self.my_user = User()
        self.upd_at = self.my_user.updated_at
        self.my_user.save()

        if self.__src in os.listdir(os.getcwd()):
            shutil.copy(self.__src, self.__dest)

    def tearDown(self):

        if self.__dest in os.listdir(os.getcwd()):
            os.remove(self.__dest)

    def test_save_works(self):
        self.assertIn(self.__src, os.listdir(os.getcwd()))

    def test_save_updated_at(self):
        self.my_user.save()
        self.assertLess(self.upd_at, self.my_user.updated_at)

    def test_save_args(self):
        with self.assertRaises(TypeError):
            self.my_user.save(None)

    def test_save_kwargs(self):
        with self.assertRaises(TypeError):
            self.my_user.save(obj=None)

if __name__ == '__main__':
    unittest.main()



