def isPrime(n):
    if n < 2:
        return False
    i = 2
    while (i*i <= n):
        if n % i == 0:
            return False
        i += 1
    return True

def evaluateQuadratic(a, b, n):
    # print(str(n) + "^2 + " + str(a) + " * " + str(n) + " + " + str(b) + " = " + str((n * n) + (a * n) + b))
    return (n * n + a * n + b)

def findLongest(number):
    longestA = 0
    longestB = 0
    longestCount = 0
    for a in range(-1 * number + 1, number):
        for b in range(-1 * number + 1, number):
            count = 0
            n = 0
            while isPrime(evaluateQuadratic(a, b, n)):
                count += 1
                if count > longestCount:
                    longestCount = count
                    longestA = a
                    longestB = b
                n += 1
    print("A: " + str(longestA) + " B: " + str(longestB) + " Count: " + str(longestCount))

findLongest(1000)