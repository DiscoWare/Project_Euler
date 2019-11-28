from math import log10
from math import floor

def getSum(n):
    exponent = floor(log10(n))
    mod = exponent + 1
    total = 0
    while (exponent >= 0):
        total += (n % (10 ** mod)) // (10 ** exponent)
        exponent -= 1
        mod -= 1
    return total

def getSumString(n):
    string = str(n)
    result = 0
    for i in range(len(string)):
        result += int(string[i])
    return result

from time import time
start = time()
result = getSum(2 ** 1000)
total = time() - start
print("Result: ", result, "    Total time: ", total)
start = time()
result = getSumString(2 ** 1000)
total = time() - start
print("String result: ", result, "Total time: ", total)

