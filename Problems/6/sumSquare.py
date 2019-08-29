def differenceSquares(n):
    squaredSum = (1 / 2 * n * (n + 1)) ** 2
    sumOfSquares = n / 6 * (2 * n + 1) * (n + 1)
    return squaredSum - sumOfSquares

n = 100
print(differenceSquares(n))