"""
Contains modelstorage tests
"""
import unittest
from os import path
from shutil import rmtree

from test_mushroom_classifier.base_test import TestBase
from mushroom_classifier.modelstorage import ModelStorage

class ModelStorageTests(TestBase):
    """"ModelStorage tests"""
    @classmethod
    def setUpClass(cls):
        currentdir = path.dirname(path.realpath(__file__))
        cls.test_dump_path = path.join(currentdir, 'model_test_dump')

    @classmethod
    def tearDownClass(cls):
        rmtree(cls.test_dump_path, ignore_errors=False)

    def test_saving_model(self):
        """Should save given model object to disk"""
        model = MockModel()
        model_storage = ModelStorage(self.test_dump_path)

        model_file_path = model_storage.save(model)
        self.assertTrue(path.isfile(model_file_path))

class MockModel():
    """Simple model object mock"""
    def __init__(self):
        return None

if __name__ == '__main__':
    unittest.main()
