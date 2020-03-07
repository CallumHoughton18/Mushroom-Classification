function [theta, minCost] = trainLogisticRegression(X,y,lambda)

% Assumes the column of 1s added to X matrix before passed to this function

[m,n] = size(X);
initTheta = zeros(n, 1);

[calcedTheta, JHistory] = gradientDescent(X, y, initTheta, 1, 600, lambda);
minCost = JHistory(end,1);

theta = calcedTheta;


endfunction