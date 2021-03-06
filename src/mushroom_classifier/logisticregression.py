"""
Contains LogisticRegression class
"""
import numpy as np
from .gradientdescent import GradientDescent
from .modelbase import ModelBase
from .mlutils import sigmoid

class LogisticRegression(ModelBase):
    """Trains model and predicts values"""
    def __init__(self, learning_rate=0.01, num_iter=500, fit_intercept=True, verbose=False):
        super(LogisticRegression, self).__init__()
        self.learning_rate = learning_rate
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose
        self.log_callback = None
        self.theta = []

    def hypothesis(self, x_matrix, theta):
        return sigmoid(np.dot(x_matrix, theta))

    def cost_function(self, hypothesis, y_vector):
        cost = (-y_vector * np.log(hypothesis) - (1 - y_vector) * np.log(1 - hypothesis)).mean()
        return cost

    def __predict_prob(self, x_vector, theta):
        if self.fit_intercept:
            x_vector = self.add_intercept(x_vector)
        return sigmoid(np.dot(x_vector, theta))

    def setup_logger(self, logger_function):
        """Sets internal log callback property"""
        self.log_callback = logger_function

    def predict(self, x_matrix, threshold=0.5):
        return self.__predict_prob(x_matrix, self.theta) >= threshold

    def train(self, x_matrix, y_vector):
        if self.fit_intercept:
            x_matrix = self.add_intercept(x_matrix)

        theta = np.zeros(x_matrix.shape[1])
        min_method = GradientDescent(self.hypothesis,
                                     self.cost_function,
                                     x_matrix, y_vector, theta,
                                     intercept_added=self.fit_intercept)

        [new_theta, costs] = min_method.calculate(num_iter=self.num_iter,
                                                  learning_rate=1, lambda_term=1)
        self.theta = theta
        if self.verbose:
            for cost in costs:
                print(f'Cost: {cost}')

        return [new_theta, costs]
