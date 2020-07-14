ls = []
base = 101
exponent = 101
for i in range(2, base):
    for j in range(2, exponent):
        ls.append(i ** j)

ls.sort()
total = 0
previous = -1
for x in ls:
    if x != previous:
        total += 1
    previous = x
print("Total: " + str(total))