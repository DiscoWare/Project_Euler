from itertools import permutations
s = "123456789"
p = permutations(s)

strings = []
for permutation in p:
    temp = ""
    for l in permutation:
        temp += l
    strings.append(temp)

products = []
sumOfProducts = 0
for permutation in strings:
    for i in range(1, len(permutation) - 1):
        for j in range(i+1, len(permutation)):
            op1 = int(permutation[0:i])
            op2 = int(permutation[i:j])
            product = int(permutation[j:len(permutation)])
            if op1 * op2 == product:
                if product not in products:
                    products.append(product)
                    print(permutation[0:i], "*", permutation[i:j], "=", permutation[j:len(permutation)])
                    sumOfProducts += product
print("Sum of products:", sumOfProducts)

