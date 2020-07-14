dic = {}
for i in range(1, 100000000000000):
    x = (10 ** i) % 1000000007 
    if x in dic:
        print("")
        print("Found repeat: " + i)
        print("")
    else:
        dic[x] = i

