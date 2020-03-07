function p = predict(theta, X)

m = size(X, 1); % Number of training examples

q = sigmoid(X*theta);
p = q >= 0.5;
end