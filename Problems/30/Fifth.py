total = 0
for i in range(2, 1000000):
    string = str(i)
    currentTotal = 0
    for j in range(len(string)):
        currentTotal += int(string[j]) ** 5
    if currentTotal == i:
        print(currentTotal)
        total += currentTotal
    currentTotal = 0
print("Total: " + str(total))

