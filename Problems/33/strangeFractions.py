def charListify(n):
    result = []
    string = str(n)
    for char in string:
        result.append(char)
    return result

def simplify(num, denom):
    from math import sqrt
    from math import floor
    for i in range(num, 0, -1):     # can be optimized
        #print("working on:", i)
        if num % i == 0 and denom % i == 0:
            #print("GCD:", i)
            return (num // i, denom // i)
            break
    return None

def generateFractions(max_denom):
    fractions = []
    for i in range(1, max_denom + 1):
        for j in range(1, i):
            fractions.append((j,i))
    return fractions

def insertIntoFractions(fractions):
    modified_fractions = []
    for i in range(1,10):
        for fraction in fractions:
            tmp_ls = [fraction]
            str_num = str(fraction[0])
            str_denom = str(fraction[1])
            str_i = str(i)
            tmp_ls.append( ( int(str_num + str_i), int(str_denom + str_i) ) )
            tmp_ls.append( ( int(str_num + str_i), int(str_i + str_denom) ) )
            tmp_ls.append( (int(str_i + str_num), int(str_i + str_denom) ) )
            tmp_ls.append( (int(str_i + str_num), int( str_denom + str_i) ) )
            modified_fractions.append(tmp_ls)
    return modified_fractions

def checkFractions(max_denom):
    simple_fractions = generateFractions(max_denom)
    fractions_ls = insertIntoFractions(simple_fractions)
    print("total fractions:", len(fractions_ls) * 4)
    special_fractions = []
    for fraction in fractions_ls:
        # print("checking:", fraction)
        reduced_og = fraction[0][0] / fraction[0][1]
        if (fraction[1][0] / fraction[1][1]) == reduced_og:
            special_fractions.append(fraction[1])
        if (fraction[2][0] / fraction[2][1]) == reduced_og:
            special_fractions.append(fraction[2])
    sum = [1, 1]
    print("special_fractions:", special_fractions)
    for fraction in special_fractions:
        sum[0] *= fraction[0]
        sum[1] *= fraction[1]
    print("sum:", sum)
    return simplify(sum[0], sum[1])

print(checkFractions(9))

sum = 0
for i in range(1,100):
    for j in range(1,i):
        sum += 1
print("total sum:", sum)
