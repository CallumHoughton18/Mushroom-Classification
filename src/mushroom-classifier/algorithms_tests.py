from algorithms import lg_gradient_descent
import numpy as np

test_X = np.random.rand(10,15)
test_y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
test_theta = np.zeros(test_X.shape[1])

lg_gradient_descent(test_X, test_y,test_theta, 1, 300, 1)