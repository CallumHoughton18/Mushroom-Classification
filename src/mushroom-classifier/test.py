import numpy as np
from sklearn import datasets
from LogisticRegression import LogisticRegression
import pickle

def log(message):
    print(message)

iris = datasets.load_iris()
X = iris.data[:, :2]
y = (iris.target != 0) * 1

randomize = np.arange(len(X))
np.random.shuffle(randomize)
X = X[randomize]
y = y[randomize]

train_X, test_X = X[:80,:], X[80:,:]
train_y, test_y = y[:80], y[80:]

model = LogisticRegression(learning_rate=0.1, num_iter=3000, verbose=True)
model.setup_logger(log)
model.train(train_X, train_y)

preds = model.predict(test_X)
accuracy = (preds == test_y).mean()
print(accuracy)

filename = "test_model.sav"
pickle.dump(model, open(filename, "wb"))

loaded_model = pickle.load(open(filename, "rb"))
loaded_accuracy = (loaded_model.predict(X) == y).mean()
print(loaded_accuracy)

