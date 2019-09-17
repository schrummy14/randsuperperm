function res = findPermList(N, numTries)

    if nargin == 0
        N = 4;
        numTries = 20000;
    end

    posPerms = getPerms(N);
    
    recordLength = inf;
    for k = 1:numTries
        curRes = randPermList(posPerms);
        curResLength = length(curRes);
        if curResLength < recordLength
            recordLength = curResLength;
            res = curRes;
        end
    end
    
end