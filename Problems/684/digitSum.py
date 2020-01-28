from time import time
from math import log10
from math import floor

timeInS = 0.0

def s(n):
    string = ""
    while n > 0:
        if n >= 9:
            string = "9" + string
            n -= 9    
        else:    
            string = str(n) + string
            n -= n
    return string

def SBrute(n):
    sum = 0
    for i in range(1, n + 1):
        sum += int(s(i))
    return sum

def Sum(n):
    return (n * (n + 1) // 2)

def S(n):
    global timeInS 
    start = time()
    exponent = floor(n / 9)
    sum = 0
    if exponent > 0:
        sum += int(n % 9) * 9
    else:
        timeInS += (time() - start)
        return Sum(n)

    while exponent >= 0:
        sum += (10 ** exponent) * 45
        sum %= 1000000007
        exponent -= 1
    timeInS += time() - start
    return sum
print("Sum of 20: " +str(S(20)))

def fib(lower, n):
    result = [0]
    curr = 1
    prev = 0
    while n > 1:
        result.append(curr)
        temp = curr
        curr = curr + prev
        prev = temp
        n -= 1
    while lower > 0:
        result.pop(0)
        lower -= 1
    print("Fib list: " + str(result))    
    return result

def digitSum(lower, n):
    lis = fib(lower, n)
    sum = 0
    count = 0
    for f in lis:
        count += 1
        sum += S(f) 
        sum = sum % 1000000007
        percentDone = count / len(lis) * 100
        print("%.f%% done. Time in S: %.2f"%(percentDone, timeInS), end='\r')
    print("")
    return sum
    
print(digitSum(2, 90))
