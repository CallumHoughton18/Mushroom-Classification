"""
Contains GradientDescent class
"""
import numpy as np

class GradientDescent():
    """Performs gradient descent calculations"""
    def __init__(self, hypothesis_function, cost_function,
                 x_matrix, y_vector, theta, intercept_added):
        self.x_matrix = x_matrix
        self.y_vector = y_vector
        self.theta = theta
        self.hypothesis_function = hypothesis_function
        self.cost_function = cost_function
        self.intercept_added = intercept_added

    def __calculate_gradient(self):
        hypothesis = self.hypothesis_function(self.x_matrix, self.theta)
        gradient = np.dot(self.x_matrix.T, (hypothesis - self.y_vector)) / self.y_vector.shape[0]
        return gradient

    def calculate(self, num_iter, learning_rate=1, lambda_term=1):
        """Performs gradient descent, returning the theta values, and cost values per iteration"""
        costs = []
        for _ in range(num_iter):
            grad = self.__calculate_gradient() + self.__calc_regulization(lambda_term)
            self.theta -= learning_rate * grad

            new_h = self.hypothesis_function(self.x_matrix, self.theta)
            costs.append(self.cost_function(new_h, self.y_vector))
        return [self.theta, costs]

    def __calc_regulization(self, lambda_term):
        theta_for_reg = None
        if self.intercept_added:
            theta_for_reg = np.copy(self.theta)
            theta_for_reg[0] = 0
        else:
            theta_for_reg = self.theta

        regularized_term = np.dot((lambda_term/self.y_vector.shape[0]), theta_for_reg)
        return regularized_term
        