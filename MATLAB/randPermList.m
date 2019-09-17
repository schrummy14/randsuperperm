function res = randPermList(posPerms)

    res = posPerms(1,:);
    posPerms(1,:) = [];
    N = length(posPerms(1,:));
    
    k = 1;
    done = false;
    
    numPosPerms = length(posPerms(:,1));
    oldk1 = res(N);
    
    while ~done
        while true
            k1 = randi(N);
            if k1 ~= oldk1
                oldk1 = k1;
                break
            end
        end
%         newPerm = [res(k+1:end) k1];
        res(end+1) = k1;
        for m = 1:numPosPerms
            if all(res((end-N+1):end) == posPerms(m,:))
                posPerms(m,:) = [];
                break
            end
        end
%         res(end+1) = k1;
        k = k + 1;
        numPosPerms = length(posPerms(:,1));
        if numPosPerms == 0
            done = true;
        end
    end
            

end