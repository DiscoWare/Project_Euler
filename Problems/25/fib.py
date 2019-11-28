def digitCount(n):
    count = 0
    while (n > 0):
        count += 1
        n //= 10
    return count

def returnIndex(digits):
    index = 1
    cur = 1
    prev = 0
    while (digitCount(cur) < digits):
        print("Current fib" + str(cur))
        cur = cur + prev
        prev = cur - prev
        index += 1

    return index

n = int(input("Digit count:"))
print("Index: " + str(returnIndex(n)))