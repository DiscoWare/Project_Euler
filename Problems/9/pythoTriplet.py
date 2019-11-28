from time import time
from math import ceil
from math import sqrt
from math import gcd

def findTripletProduct(n):
    # Mine:
    # for a in range(1, n):
    #     b = a + 1
    #     while a + b <= n - a - b:
    #         c = n - a - b
    #         if a + b + c == n and a**2 + b**2 == c**2:
    #             print(a, ", ", b, ", ", c)
    #             return a * b * c
    #         b += 1

    # Their faster:
    # for a in range(3, (n - 3) // 3):
    #     print(a)
    #     for b in range(a + 1, (n - 1 - a) // 2):
    #         c = n - a - b
    #         if a**2 + b**2 == c**2:
    #             print(a, ", ", b, ", ", c) 
    #             return a * b * c

    # Their fastest:
    s2 = n // 2
    mlimit = ceil(sqrt(s2**2)) - 1
    for m in range(2, mlimit + 1):
        if s2 % m == 0:
            sm = s2 // m 
            while sm % 2 == 0:
                sm = sm // 2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2 * m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = s2 // (k * m) 
                    n = k - m 
                    a = d*(m * m - n * n)
                    b = 2 * d * m * n 
                    c = d * (m * m + n * n) 
                    print (a, ", ", b, ", ", c) 
                k = k + 2
    return -1
                    
start = time()
print(findTripletProduct(1000000000))
stop = time()
print("Time: ", stop - start)
    