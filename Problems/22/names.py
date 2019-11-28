f = open("input.txt")
string = f.read()
f.close()
string = string.replace("\n", "")
string = string.replace('\"', '')
arr = string.split(",")
arr.sort()

total = 0
for i in range(0, len(arr)):
    print("Word:", arr[i], i, "Index")
    wordProduct = 0
    for c in arr[i]:
        print(c, "is number:", ord(c) - 64)
        wordProduct += (ord(c) - 64)
    total += (i + 1) * wordProduct
    

print(total)
