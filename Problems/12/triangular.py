from math import floor
from math import sqrt
from time import time

def generateTriangular():
    result = 0
    current = 1
    while True:
        result += current
        current += 1
        yield result

def factorize(n):
    count = 0
    for i in range(1, int(floor(sqrt(n))) + 1):
        if n % i == 0:
            count += 2
    return count

start = time()
for i in generateTriangular():
    count = factorize(i)
    if count > 500:
        break
totalTime = time() - start

print("Total time: " , totalTime)
print("Value: ", i)