import copy
import math
import time

def make2darray(n, value = 0):
    arr = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(value)
        arr.append(a)
    return arr

def printArr(arr):
    for i in arr:
        for j in i:
            print(j, ' ', end='')
        print('')

def dynamicSolve(n):
    arr = make2darray(n + 1)
    for i in range(n + 1):
        arr[i][0] = 1
        arr[0][i] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    return arr[n][n]

def factorialSolve(n):
    return (math.factorial(n + n) / (math.factorial(n) * math.factorial(n)))

def drawSolve(n):
    arr = make2darray(n + 1, value = '.')
    return recursiveDraw(arr, 0, 0)

def recursiveDraw(arr, i, j):
    count = 0
    arrCopy = copy.deepcopy(arr)
    arrCopy[i][j] = 'O'
    if i == len(arr) - 1 and j == len(arr) - 1:
        printArr(arrCopy)
        print('')
        return 1
    if (i < len(arr) - 1):
        count += recursiveDraw(arrCopy, i + 1, j)
    if (j < len(arr) - 1):
        count += recursiveDraw(arrCopy, i, j + 1)
    return count

n = int(input("How many rows and columns?\n"))
start = time.time()
# print("Total solutions: ", dynamicSolve(n))
print("Total: ", drawSolve(n))
total = time.time() - start
print("Took ", total, " seconds.")
