def myFactorial(n):
    n = int(n)
    result = n
    while n > 1:
        n -= 1
        result *= n
    return result


def factorialSum(n):
    fac = myFactorial(int(n))
    print("Factorial: ", fac)
    string = str(fac)
    result = 0
    for c in string:
        result += int(c)
    return result

while True:
    n = factorialSum(input("Number:\n"))
    print(n)
