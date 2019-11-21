function [theta, JHistory] = gradientDescent(X, y, theta, alpha, maxIters, lambda)

m = length(y);
JHistory = zeros(maxIters, 1);
alphaTerm = alpha * (1/m);

for iter = 1:maxIters
    h = sigmoid(X * theta);
    grad = (X'*(h - y))/m;

    % Don't regularize first theta, as it is for the '1' values
    thetaFoReg = theta;
    thetaFoReg(1) = 0;
    RegularizedTerm = (lambda/(m)) .* thetaFoReg;
    grad = grad + RegularizedTerm;    

    theta = theta - alpha*grad; 
    J = costFunction(theta,X, y,lambda);
    JHistory(iter) = J;
end

end