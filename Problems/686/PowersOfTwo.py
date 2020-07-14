from math import log2
from math import log10
from math import floor

def simpleP(L, n):
    originalN = n
    s = str(L)
    exponent = -1
    count = 0
    last = -1
    while n > 0:
        exponent += 1
        working = str(2 ** exponent)
        if len(working) >= len(s):
            if s == working[:len(s)]:
                percentDone = (originalN - n) / originalN * 100
                print("%.2f%% done"%percentDone, end='\r')
                n -= 1
                print(str(originalN - n) + "th exponent is " + str(exponent)) 
                if last == -1:
                    last = exponent
                else:
                    last = exponent
    return exponent

def cutDown(n, sigFigs):
    nExponent = floor(log10(n)) + 1 
    return n // (10 ** (nExponent - sigFigs))  

def P(L, n):
    from time import time
    import datetime
    start = datetime.datetime.now() 
    numberOfFigs = 20
    multiplesList = [cutDown(2 ** 196, numberOfFigs), cutDown(2 ** 289,                           numberOfFigs), cutDown(2 ** 485, numberOfFigs)]
    loopList = [196, 289, 485]
    counter = 1
    exponent = 90
    current = cutDown(2 ** 90, numberOfFigs)
    while counter < n:
        foundPattern = False
        loopIndex = 0
        for m in multiplesList:
            candidate = current * m
            candidateStr = str(candidate)
            if (candidateStr[:3] == "123"):
                foundPattern = True
                current = cutDown(candidate, numberOfFigs)
                counter += 1
                exponent += loopList[loopIndex]
                break
            loopIndex += 1
        if not foundPattern:
            print("ERROR")
    totalTime = datetime.datetime.now() - start
    totalTime = totalTime.total_seconds()
    print("Took %f seconds"%totalTime)
    return exponent

print(str(P(123, 678910)))


    

# print(str(simpleP(123, 678910)))




