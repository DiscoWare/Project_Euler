from math import sqrt
from math import floor

def getFactors(n):
    candidate = 2
    result = [1]
    while candidate <= floor(sqrt(n)):
        if n % candidate == 0:
            result.append(candidate)
            result.append(n // candidate)
        candidate += 1
    result.sort()
    return result

def divisorSum(n):
    lis = getFactors(n)
    return sum(lis)

def getAmicable(n):
    lis = []
    for i in range(1, n):
        candidate = divisorSum(i)
        if divisorSum(candidate) == i and i != candidate:
            lis.append(candidate)
    lis.sort()
    return lis


print("AMICABLE NUMBERS:" ,getAmicable(10000))
print("SUM:", sum(getAmicable(10000)))
# print(divisorSum(17))
# print(divisorSum(divisorSum(17)))