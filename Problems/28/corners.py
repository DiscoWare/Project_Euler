total = 1
current = 1
gridDimension = 3
cornerCount = 0
adder = 2

while gridDimension <= 1001:
    current += adder
    total += current
    cornerCount += 1
    if cornerCount == 4:
        cornerCount = 0
        adder += 2
        gridDimension += 2
        
print(total)
