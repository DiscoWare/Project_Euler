from math import floor

def numberToString(n):
    intStrings  = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
                   7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven",
                   12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
                   16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
    tenStrings =  {0:"", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty",
                   6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
    
    result = ""
    if floor(n / 1000):
        return "onethousand"
    if floor(n / 100):
        result += intStrings[floor(n / 100)] + "hundred"
        n %= 100
        if n > 0:
            result += "and"
    if n < 20 and n > 9:
        return result + intStrings[n]
    if floor(n / 10):
        result += tenStrings[floor(n / 10)]
        n %= 10
    result += intStrings[n]
    return result

# while True:
#     n = input("Value:\n")
#     print(numberToString(int(n)))

string = ""
for i in range(1, 1001):
    print(numberToString(i))
    string += numberToString(i)
print("Count of letters: ", len(string))
