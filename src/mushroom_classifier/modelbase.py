"""
Contains ModelBase
a base class intended for all ML models
"""
from abc import ABC, abstractmethod
from mushroom_classifier.mlutils import add_intercept

class ModelBase(ABC):
    """base class for ML models"""

    @abstractmethod
    def hypothesis(self, x_matrix, theta):
        """Hypothesis astract method"""

    @abstractmethod
    def cost_function(self, hypothesis, y_vector):
        """Hypothesis astract method"""

    @abstractmethod
    def predict(self, x_matrix, threshold):
        """Hypothesis astract method"""

    @abstractmethod
    def train(self, x_matrix, y_vector):
        """Hypothesis astract method"""

    # pylint: disable=R0201
    def add_intercept(self, x_matrix):
        """Returns x_matrix with intercept added"""
        return add_intercept(x_matrix)
