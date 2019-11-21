pkg load io;

mushroomCSVAsCells = csv2cell("mushrooms_test.csv");

[trainSet,cvSet,testSet] = preprocessing(mushroomCSVAsCells);

trainSetX = trainSet(:,2:end);
trainSetY = trainSet(:,1);

testSetX = testSet(:,2:end);
testSetY = testSet(:,1);

cvSetX = cvSet(:,2:end);
cvSetY = cvSet(:,1);


[m, n] = size(trainSetX);
[trainM, trainN] = size(testSetX);
[cvM, cvN] = size(cvSetX);

trainSetX = [ones(m, 1) trainSetX];
testSetX = [ones(trainM, 1) testSetX];
cvSetX = [ones(cvM, 1) cvSetX];
lambda = 1;

fprintf('Plotting cross validation curve...\n');
lambdaVec = [0 0.0001 0.003 0.1 0.3 1 3 5 10]';
[errorTrain, errorCV] = validationCurve(lambdaVec, trainSetX, trainSetY, cvSetX, cvSetY);
plot(lambdaVec, errorTrain, lambdaVec, errorCV);
legend('Train', 'Cross Validation');
xlabel('lambda');
ylabel('Error');

fprintf('Plotting cross learning curve...\n');
figure(2);
[errorTrainLC, ErrorCVLC] = learningCurve(trainSetX, trainSetY,cvSetX, cvSetY,lambda);
[errorLen,errorHeight] = size(errorTrainLC);
plot(1:errorLen, errorTrainLC, 1:errorLen, ErrorCVLC);
title(sprintf('Learning Curve (lambda = %f)', lambda));
xlabel('Number of training examples')
ylabel('Error')
axis([0 errorLen 0 0.5])
legend('Train', 'Cross Validation')

[theta, J] = trainLogisticRegression(trainSetX, trainSetY, lambda);
fprintf('Optimized Cost: %f\n', J);

prediction = predict(theta, testSetX);
fprintf('TAccuracy on test set (grad desc)): %f\n', mean(double(prediction == testSetY)) * 100);