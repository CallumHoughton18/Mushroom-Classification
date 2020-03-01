import numpy as np
import pickle
from LogisticRegression import LogisticRegression
from DataCleaner import DataCleaner
from TrainingDiagnostics import plot_cost

def log(message):
    print(message)

data_cleaner = DataCleaner('../files/mushrooms.csv','class','p')
[train_X, test_X, train_y, test_y]  = data_cleaner.clean()

model = LogisticRegression(learning_rate=1, num_iter=500, verbose=True)
model.setup_logger(log)
[thetas, costs] = model.train(train_X, train_y)
print('plotting costs...')
plot_cost(costs)

preds = model.predict(test_X)
accuracy = (preds == test_y).mean()
print(accuracy)

filename = "test_model.sav"
pickle.dump(model, open(filename, "wb"))

loaded_model = pickle.load(open(filename, "rb"))
loaded_accuracy = (loaded_model.predict(test_X) == test_y).mean()
print(loaded_accuracy)

