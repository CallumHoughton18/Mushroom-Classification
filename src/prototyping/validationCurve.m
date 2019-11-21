function [error_train, error_val] = validationCurve(lambdaVec, X, y, Xval, yval)

error_train = zeros(length(lambdaVec), 1);
error_val = zeros(length(lambdaVec), 1);

for i = 1:length(lambdaVec)
    lambda = lambdaVec(i);
    [thetaVector,J] = trainLogisticRegression(X, y, lambda);
    % Regularization already done through training theta vector, don't need to include it twice
    % for validation curve

    [JTrain,gradTrain] = costFunction(thetaVector, X, y, 0);
    [JVal,gradVal] = costFunction(thetaVector, Xval, yval, 0);
    error_train(i) = JTrain;
    error_val(i) = JVal;

endfor

endfunction