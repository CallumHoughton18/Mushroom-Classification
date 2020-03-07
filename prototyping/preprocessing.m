function [trainingSet,cvSet,testSet] = preprocessing(mushroomCsvCells)

processedX = [];
trainingSet = [];
cvSet = [];
testSet = [];

[rows,cols] = size(mushroomCsvCells);
for i = 1:cols
    columnValues=mushroomCsvCells(:,i);
    [~, loc] = ismember(columnValues, unique(columnValues)); %swaps labels for integers, ie ['p','e','p'] to [1,2,1]
    columnValsOneHot = label2matrix(loc',max(loc))';
    processedX = [processedX, columnValsOneHot];
endfor

% Randomely shuffle X
processedX = processedX(randperm(size(processedX, 1)), :);
trainEndRow = round(rows * 0.6);
cvSetEndRow = round(rows * 0.8);

% first column is if mushy edible, so can remove and just have y = 1 when mushroom is poisonous (ie col2)
trainingSet = processedX(1:trainEndRow,2:end);
cvSet = processedX(trainEndRow+1:cvSetEndRow,2:end);
testSet = processedX(cvSetEndRow+1:end,2:end);
endfunction