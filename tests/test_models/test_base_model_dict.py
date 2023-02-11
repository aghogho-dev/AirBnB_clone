#!/usr/bin/python3
"""Test the base_model."""
from models.base_model import BaseModel
import unittest
from datetime import datetime as dt
from time import sleep

class TestBaseModelDict(unittest.TestCase):
    """Test the instantiation of a new BaseModel."""

    def setUp(self):
        self.my_model = BaseModel()
        self.ids = [BaseModel().id for _ in range(1000)]
        self.my_model2 = BaseModel()

        self.my_model_dict = self.my_model.to_dict()
        self.dicts = [BaseModel().to_dict() for _ in range(1000)]
        self.my_model2_dict = self.my_model2.to_dict()

    def test_class_name(self):
        self.assertIsInstance(self.my_model, BaseModel, "Class should be named BaseModel")

    def test_id_str(self):
        self.assertIsInstance(self.my_model.id, str, "id instance should be a str")

    def test_created_at_datetime(self):
        self.assertIsInstance(self.my_model.created_at, dt, "created_at should be a datetime obj")

    def test_updated_at_datetime(self):
        self.assertIsInstance(self.my_model.updated_at, dt, "updated_at should be a datetime obj")

    def test_unique_id(self):
        self.assertNotIn(self.my_model.id, self.ids, "id not unique")

    def test_unique_created_at(self):
        self.assertLess(self.my_model.created_at, self.my_model2.created_at, "Time my_model was greated should be less than that of my_model2")

    def test_save(self):
        updated_at1 = self.my_model.updated_at
        self.my_model.save()
        updated_at2 = self.my_model.updated_at
        self.assertLess(updated_at1, updated_at2, "Past update should be less than recent update")

    def test_to_dict_type(self):
        self.assertIsInstance(self.my_model.to_dict(), dict, "to_dict() should return a dictionary")

    def test_to_dict_keys(self):
        the_dict = self.my_model.to_dict()
        self.assertIn("id", the_dict)
        self.assertIn("created_at", the_dict)
        self.assertIn("updated_at", the_dict)
        self.assertIn("__class__", the_dict)

    def test_to_dict_types(self):
        the_dict = self.my_model.to_dict()
        self.assertIsInstance(the_dict["id"], type(self.my_model.id))
        self.assertIsInstance(the_dict["created_at"], type(self.my_model.created_at.isoformat()))
        self.assertIsInstance(the_dict["updated_at"], type(self.my_model.updated_at.isoformat()))

    def test_str_repr(self):
        self.assertEqual(print(self.my_model), None)

    def test_more_attrs(self):
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89
        self.assertIn("name", model.to_dict())
        self.assertIn("my_number", model.to_dict())

    def test_to_dict_return(self):
        out_dict = {
                "id": self.my_model.id,
                "__class__": self.my_model.__class__.__name__,
                "created_at": self.my_model.created_at,
                "updated_at": self.my_model.updated_at
                }

        self.assertDictEqual(out_dict, self.my_model_dict)

    def test_compare_to_dict_dict_magic(self):
        self.assertNotEqual(self.my_model_dict, self.my_model.__dict__)
        self.assetNotEqual(self.my_model2_dict, self.my_model2.__dict__)

    def test_kargs(self):
        tm = dt.now()
        tm_iso = tm.isoformant()
        model = BaseModel(id="abcd-1234", created_at=tm_iso, updated_at=tm_iso)

        self.assertEqual(model.id, "abcd-1234")
        self.assertEqual(model.created_at, tm_iso)
        self.assertEqual(model.updated_at, tm_iso)

    def test_no_kargs(self):
        with self.assertRaises(TypeError):
            BaseModel(created_at=None, updated_at=None)

    def test_args(self):
        tm_iso = dt.now().isoformat()
        model = BaseModel("1234-abcd", tm_iso, tm_iso)

        self.assertNotEqual(model.id, "1234-abcd")
        self.assertNotEqaul(model.created_at, tm_iso)
        self.assertNoTeQUAL(model.updated_at, tm_iso)

    def test_arg_kwargs(self):
        tm_iso = dt.now().isoformat()
        model = BaseModel("1234-abcd", created_at=tm_iso, updatd_at=tm_iso)

        self.assertNotEqual(model.id, "1234-abcd")
        self.assertEqual(model.created_at, tm_iso)
        self.assertEqual(model.updated_at, tm_iso)


if __name__ == "__main__":
    unittest.main()
