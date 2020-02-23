import numpy as np

def lg_gradient_descent(X, y, theta, alpha, maxIters, lambdaVal):
    print(X[1])
    m=len(y)
    JHistory=np.zeros(maxIters)
    alphaTerm=alpha * (1/m)

    for iter in range(1,maxIters):
        h=sigmoid(np.dot(X, theta))
        grad=(np.transpose(X) * (h-y))/m

        thetaForReg = theta
        thetaForReg[1] = 0

        RegularizedTerm = np.dot(lambdaVal/(m), thetaForReg)
        grad = grad + RegularizedTerm
        theta = theta - alpha*grad
        #TODO: J = cost_function
        

def sigmoid(z):
    bottom_term = np.add(1, np.exp(-z))
    sigmoid = np.divide(1, bottom_term)
    return sigmoid