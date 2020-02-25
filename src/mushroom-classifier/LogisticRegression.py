import numpy as np
from GradientDescent import GradientDescent
from mlutils import sigmoid

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iter=500, fit_intercept=True):
        self.learning_rate = learning_rate
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.log_callback = lambda: None

    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)
    
    def __hypothesis(self, X, theta):
        return sigmoid(np.dot(X, theta))

    def __cost_function(self, h, y):
        cost = (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
        return cost

    def __predict_prob(self, X, theta): 
        if self.fit_intercept:
            X = self.__add_intercept(X)
            
        return sigmoid(np.dot(X, theta))

    def setup_logger(self, logger_function):
        self.log_callback = logger_function

    def predict(self, X, threshold=0.5):
        return self.__predict_prob(X, self.theta) >= threshold

    def train(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        theta = np.zeros(X.shape[1])
        min_method = GradientDescent(self.__hypothesis,
                                     self.__cost_function, 
                                     X, y, theta, 
                                     intercept_added=self.fit_intercept,
                                     log_callback=self.log_callback)

        self.theta = min_method.calculate(num_iter=3000, learning_rate=1, lambdaTerm=1)
        
        
    
