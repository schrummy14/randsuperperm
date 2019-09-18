import os
import sys
from joblib import Parallel, delayed
from findPermListHelpers import *
import time

def main(N, numTries, numCores):
    timeStart = time.time()
    if numCores > 1:
        resAll = Parallel(n_jobs=numCores)(delayed(findPermList)(N,numTries,i) for i in range(numCores))
        res = resAll[0]
        resLength = len(res)
        for curRes in resAll[1:]:
            if len(curRes) < resLength:
                resLength = len(curRes)
                res = curRes
    else:
        res = findPermList(N,numTries,0)

    print(res)
    print(len(res))
    print("Took %.2f seconds" % (time.time()-timeStart))

if __name__ == "__main__":
    nargin = len(sys.argv)
    if nargin < 4:
        print("Must provide N, numTries, and number of cores\n")
        exit()
    N = int(sys.argv[1])
    numTries = int(sys.argv[2])
    numCores = int(sys.argv[3])
    main(N, numTries, numCores)
