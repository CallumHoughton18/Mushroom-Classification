pkg load io;

mushroomCSVAsCells = csv2cell("mushrooms.csv");

[trainSet,cvSet,testSet] = preprocessing(mushroomCSVAsCells);

trainSetX = trainSet(:,2:end);
trainSetY = trainSet(:,1);

testSet = [cvSet ; testSet];

testSetX = testSet(:,2:end);
testSetY = testSet(:,1);

[m, n] = size(trainSetX);
[trainM, trainN] = size(testSetX);

trainSetX = [ones(m, 1) trainSetX];
testSetX = [ones(trainM, 1) testSetX];
lambda = 1;

[theta, J] = trainLogisticRegression(trainSetX, trainSetY, lambda);
fprintf('Optimized Cost: %f\n', J);

prediction = predict(theta, testSetX);
fprintf('Accuracy on Test Set (grad desc)): %f\n', mean(double(prediction == testSetY)) * 100);