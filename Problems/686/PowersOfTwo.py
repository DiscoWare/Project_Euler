n = 5134
s = str(n)
print(s[0])

def P(L, n):
    originalN = n
    s = str(L)
    exponent = -1
    count = 0
    last = -1
    while n > 0:
        exponent += 1
        working = str(2 ** exponent)
        if len(working) >= len(s):
            if s == working[:len(s)]:
                percentDone = (originalN - n) / originalN * 100
                print("%.2f%% done"%percentDone, end='\r')
                n -= 1
                print(str(originalN - n) + "th exponent is " + str(exponent)) 
                if last == -1:
                    last = exponent
                else:
                    # print ("Difference is: " + str(exponent - last))
                    last = exponent
    return exponent

print(str(P(123, 10)))




