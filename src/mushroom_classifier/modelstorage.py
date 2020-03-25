"""
Contains ModelStorage class
"""
from pickle import dump
from datetime import datetime
from os import path, makedirs

class ModelStorage():
    """Class for storing model and relevant files on disk"""
    def __init__(self, base_storage_folder):
        self.base_storage_folder = base_storage_folder

    def save(self, obj, objectname='model'):
        """saves given object to disk, in folder based on current time"""
        model_dir = self.__make_model_folder()
        obj_file_path = path.join(model_dir, objectname+'.sav')
        dump(obj, open(obj_file_path, 'wb'))
        return obj_file_path


    def __make_model_folder(self):
        timestamp = '{:%m-%d-%y %H:%M %S}'.format(datetime.now())
        new_model_dir = path.join(self.base_storage_folder, timestamp)

        if not path.exists(new_model_dir):
            makedirs(new_model_dir, exist_ok=True)
        return new_model_dir
