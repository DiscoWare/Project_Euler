from math import floor
from math import log10

def isPalindrome(n):
    frontExponent = floor(log10(n))
    backExponent = 1
    front = floor((n / (10 ** frontExponent)) % 10)
    back = floor((n % (10 ** backExponent)) / (10 ** (backExponent - 1))) 
    while(front == back):
        frontExponent -= 1
        backExponent += 1
        front = floor((n / (10 ** frontExponent)) % 10)
        back = floor((n % (10 ** backExponent)) / (10 ** (backExponent - 1)))
        if frontExponent < backExponent:
            return True
    return False

greatestPalindrome = 1
for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i * j):
            if i * j > greatestPalindrome:
                greatestPalindrome = i * j
print("Greatest Palindrome: ", greatestPalindrome)