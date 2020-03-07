function [J, grad] = costFunction(theta, X, y, lambda)

m = length(y); % number of training examples
J = 0;
grad = zeros(size(theta));

h = sigmoid(X*theta);
firstHalf = sum(-y' * log(h));
secondHalf = sum((1-y)' * log(1 - h));
sumPart = firstHalf - secondHalf;

scaledJ = (1/m) * sumPart;
theta(1) = 0;

RegularizedTerm = (lambda/(2*m)) * sum(theta' * theta);
J = scaledJ + RegularizedTerm;

grad = (1/m)*(X' * (h-y));
regularizedGradientTerm = (lambda/m) * theta;
grad = grad + regularizedGradientTerm;

end