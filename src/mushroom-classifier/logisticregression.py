import numpy as np
from gradientdescent import GradientDescent
from modelbase import ModelBase
from mlutils import sigmoid

class LogisticRegression(ModelBase):
    def __init__(self, learning_rate=0.01, num_iter=500, fit_intercept=True, verbose=False):
        self.learning_rate = learning_rate
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose
    
    def hypothesis(self, X, theta):
        return sigmoid(np.dot(X, theta))

    def cost_function(self, h, y):
        cost = (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
        return cost

    def __predict_prob(self, X, theta): 
        if self.fit_intercept:
            X = self.add_intercept(X)
            
        return sigmoid(np.dot(X, theta))

    def setup_logger(self, logger_function):
        self.log_callback = logger_function

    def predict(self, X, threshold=0.5):
        return self.__predict_prob(X, self.theta) >= threshold

    def train(self, X, y):
        if self.fit_intercept:
            X = self.add_intercept(X)

        theta = np.zeros(X.shape[1])
        min_method = GradientDescent(self.hypothesis,
                                     self.cost_function, 
                                     X, y, theta, 
                                     intercept_added=self.fit_intercept)

        [newTheta, costs] = min_method.calculate(num_iter=600, learning_rate=1, lambdaTerm=1)
        self.theta = theta
        if self.verbose:
            for cost in costs:
                print(f'Cost: {cost}')

        return [newTheta, costs]
        
        
    
