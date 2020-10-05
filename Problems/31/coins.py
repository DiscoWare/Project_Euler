coins = [200, 100, 50, 20, 10, 5, 2, 1]

# def split(n):
#     ls = []
#     tempCoins = coins[:]
#     if n in tempCoins:
#         tempCoins.remove(n)
#     i = 0
#     while n > 0:
#         if tempCoins[i] <= n:
#             ls.append(tempCoins[i])
#             n -= tempCoins[i]
#         else:
#             i += 1
#     return ls

# amount = 100
# ls = [amount]
# count = 0
# if amount in coins:
#     print (str(ls))
#     count += 1
# while ls[0] != 1:
#     for i in range(len(ls) - 1, -1, -1):
#         if ls[i] != 1:
#             toInsert = split(ls[i])
#             for j in range(len(toInsert)):
#                 ls.insert(i + j + 1, toInsert[j])
#             del ls[i]
#             count += 1
#             print(str(ls))
#             # input("")

# print("Total count: " + str(count))

###########################################
######### Horrendous Brute-Force
###########################################

n = 200
count = 0
for a in range(0, n + 1, 200):
    for b in range(a, n + 1, 100):
        for c in range(b, n + 1, 50):
            for d in range(c, n + 1, 20):
                for e in range(d, n + 1, 10):
                    for f in range(e, n + 1, 5):
                        for g in range(f, n + 1, 2):
                            count += 1
print(count)


