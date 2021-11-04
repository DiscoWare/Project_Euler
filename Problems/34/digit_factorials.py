from math import factorial 

i = 10
while True:
    str_i = str(i)
    sum = 0
    for j in range(len(str_i)):
        sum += factorial(int(str_i[j]))
    if sum == i:
        print(sum)
    i += 1