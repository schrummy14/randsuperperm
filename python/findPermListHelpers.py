
from itertools import permutations
import random
from tqdm import tqdm

def getPerms(N):
    perms = list(permutations(range(1, N+1))) 
    return perms

def randPermListSmart(posPerms):
    res = list(posPerms[0])
    posPerms.remove(tuple(res))
    N = res[-1]
    done = False
    numPosPerms = len(posPerms)
    oldk1 = N

    while not done:
        # Find possible next perms
        posID = []
        kk = 0
        for perm in posPerms:
            if list(perm[0:(N-1)]) == res[-(N-1):]:
                posID.append(kk)
            kk += 1
        if len(posID) > 0:
            newID = posID[random.randint(0,len(posID)-1)]
            newVal = posPerms[newID][-1]
            posPerms.remove(posPerms[newID])
        else:
            oldVal = res[-1]
            while True:
                newVal = random.randint(1,N)
                if newVal != oldVal:
                    break
        res.append(newVal)
        numPosPerms = len(posPerms)
        if numPosPerms == 0:
            done = True
    return res
            

def randPermList(posPerms):
    res = list(posPerms[0])
    posPerms.remove(tuple(res))
    N = res[-1]
    done = False
    numPosPerms = len(posPerms)
    oldk1 = N

    while not done:
        while True:
            k1 = random.randint(1,N)
            if k1 != oldk1:
                oldk1 = k1
                break
        res.append(k1)
        for perm in posPerms:
            if list(perm) == res[-N:]:
                posPerms.remove(perm)
                break

        numPosPerms = len(posPerms)
        if numPosPerms == 0:
            done = True
    
    return res

def findPermList(N, numTries, coreID):
    posPerms = getPerms(N)

    res = []
    for perm in posPerms:
        for k in perm:
            res.append(k)
    recordLength = len(res)

    for k in tqdm(range(numTries)):
        curRes = randPermListSmart(posPerms.copy())
        curResLength = len(curRes)
        if curResLength < recordLength:
            recordLength = curResLength
            res = curRes
            write2file(res, recordLength, coreID)
    return res

def write2file(res, resLength, coreID):
    with open("resProc" + str(coreID) + ".txt","w") as f:
        f.write(str(resLength) + "\n")
        f.write(str(res) + "\n")