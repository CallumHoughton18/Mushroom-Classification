#pylint: disable=wrong-import-position
#pylint: disable=invalid-name

# This method contains a fair amount of duplication and is longer than it needs to be
# This has been left this way to see more easily the actual workflow of training a model
# And then saving and exporting it for later use
"""
End to end training of model, auto deploys to current_model
folder if model is accurate enough
"""
from pickle import load
from shutil import rmtree, copytree
from os import path, makedirs

import numpy as np
import pandas as pd

from mushroom_classifier.logisticregression import LogisticRegression
from mushroom_classifier.datacleaner import DataCleaner
from mushroom_classifier.trainingdiagnostics import TrainingDiagnostics
from mushroom_classifier.modelstorage import ModelStorage
from mushroom_classifier.path_constants import DATASET_DIR, CURRENT_MODEL_DIR, TRAINED_MODELS_DIR

def log(message):
    """Performs logging of given message"""
    print(message)

print(DATASET_DIR)
models_folder = TRAINED_MODELS_DIR
dataset_path = path.join(DATASET_DIR, 'mushrooms.csv')
training_diagnostics = TrainingDiagnostics()
model_storage = ModelStorage(models_folder)
dataset = pd.read_csv(dataset_path)
data_cleaner = DataCleaner(dataset, 'class', 'p')

log('cleaning data...')
# Typically would want a cross validation set to optimize learning rate and regularization
# but as these parameters are fine as is, the splitting just gives a train and test set
[train_X, test_X, train_y, test_y] = data_cleaner.clean()

log('plotting learning curve...')
model = LogisticRegression(learning_rate=1, num_iter=500, fit_intercept=False)
training_diagnostics.plot_learning_curve(train_X, train_y,
                                         test_X, test_y, model, max_training_size=2500)

log('training actual model...')
model.fit_intercept = True
[thetas, costs] = model.train(train_X, train_y)
training_diagnostics.plot_cost(costs)

preds = model.predict(test_X)
in_mem_accuracy = (preds == test_y).mean()
log(f'In memory accuracy: {in_mem_accuracy}')
assert in_mem_accuracy > 0.95

model_file_path = model_storage.save(model)
columns_file_path = model_storage.save(data_cleaner.columns_for_index, 'columns_for_index')
training_diagnostics.save_diagostics(path.dirname(model_file_path))

loaded_model = load(open(model_file_path, 'rb'))
loaded_columns = load(open(columns_file_path, 'rb'))

loaded_preds = loaded_model.predict(test_X)
loaded_accuracy = (preds == test_y).mean()
log(f'Loaded model accuracy: {loaded_accuracy}')
assert loaded_accuracy > 0.95

data_cleaner = DataCleaner(dataset, 'class', 'p')
data_cleaner.columns_for_index = loaded_columns

unseen_test_data_path = path.join(DATASET_DIR, 'unseen_mushrooms.csv')
unseen_test_data = pd.read_csv(unseen_test_data_path)
unseen_test_data_cleaned = data_cleaner.clean_new_unseen_data(unseen_test_data)
unseen_preds = loaded_model.predict(unseen_test_data_cleaned)

np.testing.assert_array_equal(unseen_preds, [True, False],
                              'Predictions not accurate for unseen_mushrooms, model not exported')

if not path.exists(CURRENT_MODEL_DIR):
    makedirs(CURRENT_MODEL_DIR)

rmtree(CURRENT_MODEL_DIR)
copytree(path.dirname(model_file_path), CURRENT_MODEL_DIR)
