coins = [200, 100, 50, 20, 10, 5, 2, 1]

def split(n):
    ls = []
    tempCoins = coins[:]
    if n in tempCoins:
        tempCoins.remove(n)
    i = 0
    while n > 0:
        if tempCoins[i] <= n:
            ls.append(tempCoins[i])
            n -= tempCoins[i]
        else:
            i += 1
    return ls

def stripOnes(ls):
    for i in range(len(ls) - 1, -1, -1):
        if ls[i] == 1:
            del ls[i]
        else:
            break
    return ls

# print(split(8))
# print(stripOnes([3, 2, 1, 1, 1, 1]))

amount = 200
ls = [amount]
count = 0
if amount in coins:
    print (str(ls))
    count += 1
while ls[0] != 1:
    i = len(ls) - 1
    while ls[i] == 1:
        i -= 1
    toInsert = split(ls[i])
    for j in range(len(toInsert)):
        ls.insert(i + j + 1, toInsert[j])
    del ls[i]
    count += 1
    print(str(ls))
    # input("")

print("Total count: " + str(count))





