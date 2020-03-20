import numpy as np
import pandas as pd
from os import path

from mushroom_classifier.logisticregression import LogisticRegression
from mushroom_classifier.datacleaner import DataCleaner
from mushroom_classifier.trainingdiagnostics import TrainingDiagnostics
from mushroom_classifier.modelstorage import ModelStorage

def log(message):
    print(message)

training_diagnostics = TrainingDiagnostics()
model_storage = ModelStorage("./trained_models")
dataset = pd.read_csv('./files/mushrooms.csv')
data_cleaner = DataCleaner(dataset,'class','p')
[train_X, test_X, train_y, test_y]  = data_cleaner.clean()

model = LogisticRegression(learning_rate=1, num_iter=500, fit_intercept=False)
training_diagnostics.plot_learning_curve(train_X, train_y, test_X, test_y, model, max_training_size=3000)

model.setup_logger(log)
model.fit_intercept = True
[thetas, costs] = model.train(train_X, train_y)
training_diagnostics.plot_cost(costs)

preds = model.predict(test_X)
accuracy = (preds == test_y).mean()
print(accuracy)

model_file_path = model_storage.save(model)
training_diagnostics.save_diagostics(path.dirname(model_file_path))

