def threeten(n):
    current = 3
    sum = 0
    while current < n:
        sum += current
        current += 3

    current = 5
    while current < n:
        if (current % 3) != 0:
            sum += current
        current += 5
    return sum

print ('Value is: ', threeten(1000))