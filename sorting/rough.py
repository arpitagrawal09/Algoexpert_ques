def insertionSort(array):
    l = len(array)
    nOS = 0
    i = 0
    while(i < l):
        e = array[i]
        j = l-1
        while((j>=i)):
            if(i==j):
                i += 1
                nOS += 1
                break
            adj = array[j]
            if(adj > e):
                j-=1
            else: 
                array.insert(j+1, e)
                del array[i]
                nOS += 1
                break
        if nOS == l - 1: break
    return array 

array1 = [3, 2, 1]
array2 = [8, 5, 2, 9, 5, 6, 3]
print(insertionSort(array2))