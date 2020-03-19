from pickle import dump
from datetime import datetime
from os import path, makedirs

class ModelStorage():
    def __init__(self, base_storage_folder):
        self.base_storage_folder = base_storage_folder

    def save(self, model):
        model_dir = self.__make_model_folder()
        model_file_path = path.join(model_dir, 'model.sav')
        dump(model, open(model_file_path, "wb"))
        return model_file_path


    def __make_model_folder(self):
        timestamp = '{:%m-%d-%y %H:%M %S}'.format(datetime.now())
        new_model_dir = path.join(self.base_storage_folder, timestamp)
        makedirs(new_model_dir)
        return new_model_dir


