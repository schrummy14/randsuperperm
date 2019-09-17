
from itertools import permutations
import random

def getPerms(N):
    perms = list(permutations(range(1, N+1))) 
    return perms

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

def findPermList(N, numTries):
    posPerms = getPerms(N)

    res = []
    for perm in posPerms:
        for k in perm:
            res.append(k)
    recordLength = len(res)

    for k in range(numTries):
        curRes = randPermList(posPerms.copy())
        curResLength = len(curRes)
        if curResLength < recordLength:
            recordLength = curResLength
            res = curRes
    return res
