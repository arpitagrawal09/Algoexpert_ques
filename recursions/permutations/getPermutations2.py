def getPermutations(array):
    
    l = len(array)
    if(l==1): return array
    allPerms = []
    for i in range(1, l):
        arr1 = array[0:i]
        arr2 = array[i:]
        arr1 = getPermutations(arr1)
        arr2 = getPermutations(arr2)
        for j in range(len(arr1)):
            for k in range(len(arr2)):
                perm1 = arr1[j]
                perm2 = arr2[k]     
                allPerms.append(perm1+perm2)
                allPerms.append(perm2+perm1)
    uniquePerms = []                   
    [uniquePerms.append(x) for x in allPerms if x not in uniquePerms]
    return uniquePerms
    
array1 = [1, 2, 3]
array2 = [5]
array3 = [1, 2]
print(getPermutations(array3))