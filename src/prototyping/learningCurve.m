function [error_train, error_val] = learningCurve(X, y, Xval, yval, lambda)

m = size(X, 1);
error_train = zeros(m, 1);
error_val   = zeros(m, 1);

for i = 1:m
    XSubset = X(1:i, :);
    ySubset = y(1:i);
    thetaVector = trainLogisticRegression(XSubset, ySubset, lambda);

    [costFunctionTrain,gradTrain] = costFunction(thetaVector, XSubset, ySubset, 0);
    error_train(i) = costFunctionTrain;

    [costFunctionVal, gradVal] = costFunction(thetaVector, Xval, yval, 0);
    error_val(i) = costFunctionVal;      
end

endfunction