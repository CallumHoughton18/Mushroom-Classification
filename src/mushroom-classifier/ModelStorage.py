import pickle
import datetime as dt
import os 

class ModelStorage():
    def __init__(self, base_storage_folder):
        self.base_storage_folder = base_storage_folder

    def save(self, model):
        model_dir = self.__make_model_folder()
        model_file_path = os.path.join(model_dir, 'model.sav')
        pickle.dump(model, open(model_file_path, "wb"))
        return model_file_path


    def __make_model_folder(self):
        timestamp = '{:%m-%d-%y %H:%M %S}'.format(dt.datetime.now())
        new_model_dir = os.path.join(self.base_storage_folder, timestamp)
        os.makedirs(new_model_dir)
        return new_model_dir


