import numpy as np
from logisticregression import LogisticRegression
from datacleaner import DataCleaner
from trainingdiagnostics import TrainingDiagnostics
from modelstorage import ModelStorage
import os.path as path

def log(message):
    print(message)

training_diagnostics = TrainingDiagnostics()
model_storage = ModelStorage("./trained_models")
data_cleaner = DataCleaner('../files/mushrooms.csv','class','p')
[train_X, test_X, train_y, test_y]  = data_cleaner.clean()

model_for_learning_curve = LogisticRegression(learning_rate=1, num_iter=500, verbose=False, fit_intercept=False)
training_diagnostics.plot_learning_curve(train_X, train_y, test_X, test_y, model_for_learning_curve, max_training_size=3000)

model = LogisticRegression(learning_rate=1, num_iter=500, verbose=True)
model.setup_logger(log)
[thetas, costs] = model.train(train_X, train_y)
training_diagnostics.plot_cost(costs)

preds = model.predict(test_X)
accuracy = (preds == test_y).mean()
print(accuracy)

model_file_path = model_storage.save(model)
model_dir = path.dirname(model_file_path)
training_diagnostics.save_diagostics(model_dir)

