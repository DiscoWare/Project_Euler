def myDivision(n):
    remainder = 10
    result = ""
    for i in range(2 * n):
        result += str(remainder // n)
        remainder = (remainder % n) * 10
    return result

def longestSlice(n):
    String = myDivision(n)
    while String[:1] == "0":
        String = String[1:]
    size = 1
    longestStr = ""
    while (size < n):
        subStr1 = String[:size]
        subStr2 = String[size:size+size]
        if subStr1 == subStr2:
            if len(longestStr) == 0:
                longestStr = subStr1
            elif subStr1 != (len(subStr1)) // (len(longestStr)) * longestStr:
                longestStr = subStr1
                return longestStr
        size += 1
    return longestStr

from time import time
start = time()
longest = ""
longestInt = int
for i in range(1, 1000):
    current = longestSlice(i)
    if len(current) > len(longest):
        longest = current
        longestInt = i
end = time()
print("Denominator: " + str(longestInt) + " with a repeating value of: " + longest)
print("Time taken: " + str(end - start))




    