from abc import ABC, abstractmethod
import numpy as np

class ModelBase(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def hypothesis(self, X, theta):
        pass
    
    @abstractmethod
    def cost_function(self, h, y):
        pass

    @abstractmethod
    def predict(self, X, threshold):
        pass

    @abstractmethod
    def train(self, X, y):
        pass

    def add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)


