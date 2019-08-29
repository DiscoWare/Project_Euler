def maxPrimeFactor(n):
    lastFactor = 1
    candidate = 2
    while n > 1:
        if n % candidate == 0:
            lastFactor = candidate
            while n % lastFactor == 0:
                n = n / lastFactor
        candidate += 1
    return lastFactor


n = 600851475143
print("Largest prime factor of ", n, ": ", maxPrimeFactor(n))



