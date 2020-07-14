def countSequence(n):
    count = 0
    original = n
    while n != 1:
        if n in counted:
            count += counted[n]
            break
        if (n % 2 == 0):
            n = n // 2
        else :
            n = 3*n + 1
        count += 1
    counted[original] = count
    return count

def countBruteForce(n):
    count = 0
    original = n
    while n != 1:
        if (n % 2 == 0):
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

counted = {}
counted[1] = 1
from time import time
start = time()
biggestCount = 0
for i in range(1, 1000000):
    currentCount = countSequence(i)
    if currentCount > biggestCount:
        biggestCount = currentCount
        number = i

totalTime = time() - start
print("Largest number: ", number, " Count: ", biggestCount, " Total time: ", totalTime)
