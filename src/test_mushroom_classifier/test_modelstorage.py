import unittest
from test_mushroom_classifier.base_test import TestBase
from mushroom_classifier.modelstorage import ModelStorage
from os import path
from shutil import rmtree

class ModelStorageTests(TestBase):
    
    @classmethod
    def setUpClass(cls):
        currentdir = path.dirname(path.realpath(__file__))
        cls.test_dump_path = path.join(currentdir,"model_test_dump")

    @classmethod
    def tearDownClass(cls):
        rmtree(cls.test_dump_path, ignore_errors = False)  

    def test_saving_model(self):
        model = MockModel()
        model_storage = ModelStorage(self.test_dump_path)

        model_file_path = model_storage.save(model)
        self.assertTrue(path.isfile(model_file_path))

class MockModel():
    def __init__(self):
        return None
        
if __name__ == "__main__":
    unittest.main()