import os
from joblib import Parallel, delayed
from findPermListHelpers import *
import time

numCores = 1
N = 4
numTries = 200000

timeStart = time.time()
if numCores > 1:
    resAll = Parallel(n_jobs=numCores)(delayed(findPermList)(N,numTries) for i in range(numCores))
    res = resAll[0]
    resLength = len(res)
    for curRes in resAll[1:]:
        if len(curRes) < resLength:
            resLength = len(curRes)
            res = curRes
else:
    res = findPermList(N,numTries)

print(res)
print(len(res))
print("Took %.2f seconds" % (time.time()-timeStart))