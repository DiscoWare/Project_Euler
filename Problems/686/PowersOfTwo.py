from math import log2
def P(L, n):
    originalN = n
    s = str(L)
    exponent = 90
    current = 2 ** 90
    a = 2 ** 196
    b = 2 ** 289
    c = 2 ** 485
    multiplierList = [a, b, c]
    while n > 1:
        for m in multiplierList:
            candidate = current * m
            strCandidate = str(candidate)
            if strCandidate[:3] == "123":
                current = candidate
                # print(str(log2(candidate)))
                break
        n -= 1
        if n % 100 == 0:
            percent = (originalN - n) / originalN * 100
            print("%.2f%% done."%percent, end = '\r')

    return log2(current)

print("Hi")
print(str(P(123, 678910)))




