from time import time

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

start = time()        
def sumOfPrimes(max):
    primes = eratosthenes(max - 1)
    sum = 0
    for p in primes:
        sum += p

    return sum
totalTime = time() - start

n = 2000000
print("Sum of primes under ", n, " is: ", sumOfPrimes(n))
print("Total time: ", totalTime)
print(eratosthenes(1000000))



