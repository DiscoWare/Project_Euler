from math import floor
from math import sqrt

def getFactors(n):
    candidate = 2
    result = [1]
    while candidate <= floor(sqrt(n)):
        if n % candidate == 0:
            result.append(candidate)
            result.append(n // candidate)
        candidate += 1
    if sqrt(n) == floor(sqrt(n)):
        result.remove(sqrt(n))
    result.sort()
    return result

def isAbundant(n):
    return sum(getFactors(n)) > n

def getAbundants(n):
    abundants = []
    for i in range(12, n):
        if isAbundant(i):
            abundants.append(i)
    return abundants

def sumNonAbundants(max = 20161):           # last non abundant sum, determined experimentally
    abundants = getAbundants(max + 1)
    numbers = {}
    for i in range(1, max + 1):
        numbers[i] = False       

    for i in range(0, len(abundants)):
        for j in range(i, len(abundants)):
            candidate = abundants[i] + abundants[j]
            if candidate <= max:
                numbers[candidate] = True

    sum = 0
    for i in range(1, max + 1):
        if not numbers[i]:
            sum += i

    #///////////////////////
    # For finding max non 
    #    abundant sum
    #//////////////////////

    # for e in numbers:
    #     if numbers[e] == False:
    #         lastOne = e
    # print("Last non sum:", lastOne)

    return sum

print(sumNonAbundants())
