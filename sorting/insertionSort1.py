
def insertionSort(array):
    l = len(array)
    #nSettledPairs = 0
    change = l-1
    while(change > 0):
        #nSettledPairs = 0 
        change = 0       
        for i in range(l):
            target = array[i]
            j = l - 1 
            while((j<l) & (j>i)):
                ele = array[j]
                if(target > ele):
                    array.remove(target)
                    array.insert(j, target)
                    #nSettledPairs += 1
                    change += 1      
                    break
                elif(target == ele):
                    if(j != i + 1):
                        #array.remove(target)
                        del array[i]
                        array.insert(j, target)
                        #nSettledPairs += 1
                        change += 1      
                    break                    
                else:
                    j -= 1
                    #nSettledPairs += 1 
    return array

"""def insertionSort(array):
    l = len(array)
    nSettledPairs = 0
    while(nSettledPairs != l - 1)
    for i in range(l):
        target = array[i]
        nSettledPairs = 0
        j = l - 1 
        while(j<l) :
            ele = array[j]
            if(target >= ele):
                array.remove(target)
                array.append(target)
                nSettledPair += 1      
                break
            else:
                j -= 1
        if(nSettledPairs == l - 1):
            return array """


array1 = [6, 6, 6, 5]
array2 = [3, 9, 8, 4]
array3 = [8, 5, 2, 9, 5, 6, 3]
array4 = [1]
print(insertionSort(array3))
