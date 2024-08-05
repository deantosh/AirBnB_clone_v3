#!/usr/bin/python3
"""
Module defines a test for DBStorage class
"""
from datetime import datetime
import inspect
import models import storage_type
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


@unittest.skipIf(storage_type != 'db', "Testing database storage only")
class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    def test_all_returns_dict(self):
        """Test that all method: returns a dictionaty"""

    def test_all_no_class(self):
        """
        Test that all method:
            returns all rows when no class is passed
        """

    def test_new(self):
        """Test that new method: adds an object to the database"""

    def test_save(self):
        """
        Test that save method:
            properly saves objects to the database
        """

    def test_delete(self):
        """
        Test that delete method:
            deletes object from current database session
        """

    def test_reload(self):
        """
        Test that reload method:
            creates all table in the current database session
        """

    def test_close(self):
        """
        Test that the close method:
            closes the current database session
        """

    def test_get(self):
        """
        Test get():
             gets an object of specified id from storage
        """

    def test_count(self):
        """
        Test count():
            counts the number of all objects or class objects
        """
