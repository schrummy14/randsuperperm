clear
clc

numCores = 1;
N = 4;
numTries = 10000;

res = cell(numCores,1);

if numCores > 1
    try
        parpool(numCores);
    catch
        disp('ParPool has already been started')
    end
    tic;
    parfor k = 1:numCores
        res{k} = findPermList(N,numTries);
    end
    minLength = inf;
    for k = 1:numCores
        if length(res{k}) < minLength
            minLength = length(res{k});
            minRes = res{k};
        end
    end
else
    tic;
    minRes = findPermList(N,numTries);
end

toc
    
