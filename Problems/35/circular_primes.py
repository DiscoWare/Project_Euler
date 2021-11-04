s = "abcd"

def eratosthenes(max):
    arr = bytearray(max - 1)
    for i in range(0, max - 1):
        arr[i] = True
    done = False

    factor = 2
    for i in range(0, max - 1):
        if done:
            break
        workingIndex = i + factor
        if arr[i]:
            done = True
            while workingIndex < max - 1:
                if arr[workingIndex]:
                    done = False
                    arr[workingIndex] = False
                workingIndex += factor
        factor += 1

    primeList = []
    currentNum = 2
    for i in range(0, max - 1):
        if arr[i] == True:
            primeList.append(currentNum)
        currentNum += 1
    return primeList

def return_rotations(i):
    s = str(i)
    result = []
    for i in range(len(s)):
        temp_str = "";
        for j in range(len(s)):
            temp_str += s[(i + j) % len(s)]
        result.append(int(temp_str))
    return result

primes = eratosthenes(1000000)

count = 0
for prime in primes:
    is_circular_prime = True
    for rotation in return_rotations(prime):
        if not (rotation in primes):
            is_circular_prime = False
            break 
    if is_circular_prime:
        print(prime)
        count += 1

print("Count:", count)


