import numpy as np

class GradientDescent():
    def __init__(self, hypothesis_function, cost_function, X, y, theta, intercept_added, log_callback):
        self.X = X
        self.y = y
        self.theta = theta
        self.hypothesis_function = hypothesis_function
        self.cost_function = cost_function
        self.intercept_added = intercept_added
        self.log_callback = log_callback

    def __calculate_gradient(self):
        h = self.hypothesis_function(self.X, self.theta)
        gradient = np.dot(self.X.T, (h - self.y)) / self.y.shape[0]
        return gradient

    def calculate(self, num_iter, learning_rate=1, lambdaTerm=1):
        for i in range(num_iter):
            grad = self.__calculate_gradient() + self.__calc_regulization(lambdaTerm)
            self.theta -= grad * learning_rate

            if self.log_callback:
                new_h=self.hypothesis_function(self.X, self.theta)
                self.log_callback(f'loss: {self.cost_function(new_h, self.y)}\t')
        return self.theta

    def __calc_regulization(self, lambdaTerm):
        theta_for_reg = self.theta[:1:] if self.intercept_added else self.theta
        regularlizedTerm = np.dot((lambdaTerm/self.y.shape[0]), theta_for_reg)
        return regularlizedTerm





