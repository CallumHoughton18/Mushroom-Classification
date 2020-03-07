from abc import ABC, abstractmethod
from mushroom_classifier.mlutils import add_intercept
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
        return add_intercept(X)





