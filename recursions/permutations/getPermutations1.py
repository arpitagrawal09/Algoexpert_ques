def getPermutations(array):
    # Write your code here.
    l = len(array)
    if(l==1): return array
    else:
        part1 = [array[0]] 
        part2 = array[1:]
        print(part1)
        print(part2)        
        if(len(part2)==1):
            e1 = part1[0]
            e2 = part2[0]
            uniquePerms = [[e1, e2], [e2, e1]]
        part2 = getPermutations(part2)
        #print(part2)
        allPermutations = []
        uniquePerms = []
        if(len(part2)>1):
            for i in range(len(part2)):
                thisPermutation = part2[i]
                print(thisPermutation)
                allPermutations.append(part1+thisPermutation)
                allPermutations.append(thisPermutation+part1)
            print(allPermutations)
            [uniquePerms.append(x) for x in allPermutations if x not in uniquePerms]
        return uniquePerms
    
array1 = [1, 2, 3]
array2 = [8]
array3 = [1, 2]
print(getPermutations(array1))