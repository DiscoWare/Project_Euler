def isPrime(n):
    i = 2
    while i ** 2 <= n:
        if (n % i == 0):
            return False
        i += 1
    print(n)
    return True

def nthPrime(n):
    count = 1
    current = 2
    while count < n:
        current += 1
        if isPrime(current):
            count += 1

    return current

print(nthPrime(10001))

