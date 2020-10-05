def charListify(n):
    result = []
    string = str(n)
    for char in string:
        result.append(char)
    return result

def simplify(num, denom):
    from math import sqrt
    from math import floor
    for i in range(num, 1, -1):     # can be optimized
        print("working on:", i)
        if num % i == 0 and denom % i == 0:
            print("GCD:", i)
            return (num // i, denom // i)
            break
    return (num, denom)

print(simplify(12, 36))

# def cancelIncorrectly(numerator, denominator):
#     nList = charListify(numerator)
#     dList = charListify(denominator)
#     for n in nList:
#         for d in dList:


# max = 500
# for i in range(1, max - 1):
#     for j in range(i, max):
#         fraction = i / j
#         cancelled = cancel(fraction)
#         if (cancelled == fraction):
#             print(i, "/", j, "==", cancelled)

# cancel(123, 124)
