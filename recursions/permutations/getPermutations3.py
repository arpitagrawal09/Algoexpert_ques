def getPermutations(array):
    l = len(array)
    if l <= 1 : return [array]
    if l == 2 :
        ans = [[array[0], array[1]], [array[1], array[0]]]
        return ans
    allPerms = []
    uniquePerms = []
    for i in range(1, l):
        arrLeft = array[0:i]
        arrRight = array[i:]
        permsLeft = getPermutations(arrLeft)
        permsRight = getPermutations(arrRight)
        for permL in permsLeft:
            for permR in permsRight:
                p1 = permL + permR
                p2 = permR + permL
                #p = p1 + p2
                #uniquePerms += p
                allPerms.append(p1)
                allPerms.append(p2)
    [uniquePerms.append(perm) for perm in allPerms if perm not in uniquePerms]
    return uniquePerms

num1 = [1]
num2 = [2, 1]
num3 = [3, 1, 2]
print(getPermutations(num3))
