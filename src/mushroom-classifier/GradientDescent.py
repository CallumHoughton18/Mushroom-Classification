import numpy as np

class GradientDescent():
    def __init__(self, hypothesis_function, cost_function, X, y, theta, intercept_added):
        self.X = X
        self.y = y
        self.theta = theta
        self.hypothesis_function = hypothesis_function
        self.cost_function = cost_function
        self.intercept_added = intercept_added

    def __calculate_gradient(self):
        h = self.hypothesis_function(self.X, self.theta)
        gradient = np.dot(self.X.T, (h - self.y)) / self.y.shape[0]
        return gradient

    def calculate(self, num_iter, learning_rate=1, lambdaTerm=1):
        costs = []
        for i in range(num_iter):
            grad = self.__calculate_gradient() + self.__calc_regulization(lambdaTerm)
            self.theta -= learning_rate * grad

            new_h=self.hypothesis_function(self.X, self.theta)
            costs.append(self.cost_function(new_h, self.y))
        return [self.theta, costs]

    def __calc_regulization(self, lambdaTerm):
        theta_for_reg = self.theta[:1:] if self.intercept_added else self.theta
        regularlizedTerm = np.dot((lambdaTerm/self.y.shape[0]), theta_for_reg)
        return regularlizedTerm





