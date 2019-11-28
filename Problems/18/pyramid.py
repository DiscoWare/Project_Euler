def make2dArray(fileName):
    with open(fileName) as inp:
        lines = inp.readlines()
    lines = [x.strip() for x in lines]
    result = []
    for line in lines:
        row = []
        number = ""
        for i in range(len(line)):
            if line[i] == " ":
                row.append(int(number))
                number = ""
            elif i == len(line) - 1:
                number += line[i]
                row.append(int(number))
                number = ""
            else:
                number += line[i]
        result.append(row)
    return result

def findMaxSum(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr[i])):
            if j == 0:
                arr[i][j] += arr[i - 1][0]
            elif j == len(arr[i]) - 1:
                arr[i][j] += arr[i - 1][j - 1]
            else:
                arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])
    return max(arr[len(arr) - 1])

from time import time
start = time()
arr = make2dArray("input.txt")
result = findMaxSum(arr)
total = time() - start
print("\nMax Sum is: ", result, "\nTime taken: ", 1000 * total, " milliseconds")