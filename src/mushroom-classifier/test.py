import numpy as np
import pickle
from LogisticRegression import LogisticRegression
from DataCleaner import DataCleaner
from TrainingDiagnostics import TrainingDiagnostics

def log(message):
    print(message)
    
training_diagnostics = TrainingDiagnostics()
data_cleaner = DataCleaner('../files/mushrooms.csv','class','p')
[train_X, test_X, train_y, test_y]  = data_cleaner.clean()

model_for_learning_curve = LogisticRegression(learning_rate=1, num_iter=500, verbose=False, fit_intercept=False)
training_diagnostics.plot_learning_curve(train_X, train_y, test_X, test_y, model_for_learning_curve, max_training_size=3000)

model = LogisticRegression(learning_rate=1, num_iter=500, verbose=True)
model.setup_logger(log)
[thetas, costs] = model.train(train_X, train_y)
training_diagnostics.plot_cost(costs)

training_diagnostics.save_diagostics('./')

preds = model.predict(test_X)
accuracy = (preds == test_y).mean()
print(accuracy)

filename = "test_model.sav"
pickle.dump(model, open(filename, "wb"))

loaded_model = pickle.load(open(filename, "rb"))
loaded_accuracy = (loaded_model.predict(test_X) == test_y).mean()
print(loaded_accuracy)

