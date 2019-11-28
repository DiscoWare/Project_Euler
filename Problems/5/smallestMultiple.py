from math import sqrt
from math import floor
from time import time
from math import log10

def eratosthenes(max):
    arr = bytearray(max - 1)
    for i in range(0, max - 1):
        arr[i] = True
    done = False

    factor = 2
    for i in range(0, max - 1):
        if done:
            break
        workingIndex = i + factor
        if arr[i]:
            done = True
            while workingIndex < max - 1:
                if arr[workingIndex]:
                    done = False
                    arr[workingIndex] = False
                workingIndex += factor
        factor += 1

    primeList = []
    currentNum = 2
    for i in range(0, max - 1):
        if arr[i] == True:
            primeList.append(currentNum)
        currentNum += 1
    return primeList

def smallestMultiple(n):
    primes = eratosthenes(n)
    counts = {}
    max = floor(sqrt(n))
    result = 1
    for p in primes:
        counts[p] = 1
        if p <= max:
            counts[p] = floor(log10(n) / log10(p))
        result *= p ** counts[p]
    print(counts)
    return result


    

start = time()
print(smallestMultiple(20))
print("Total time: ", time() - start)

