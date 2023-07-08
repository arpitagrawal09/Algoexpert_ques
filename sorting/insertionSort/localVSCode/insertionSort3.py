def insertionSort(array):
    l = len(array)
    correctPairs = 0
    i = 0
    while(i < l):
        e = array[i]
        if(i==1): print(array)
        j = l-1
        while((j>=i)):
            if(i==j):
                i += 1
                correctPairs += 1
                break
            adj = array[j]
            if(adj > e):
                j-=1
            elif(adj<e): 
                array.insert(j+1, e)
                del array[i]
                correctPairs += 1
                break
            else:
                k = j - 1
                while(k>=i):
                    if(array[k] != e):
                        break
                    k -= 1  
                array.insert(j+1, e)
                correctPairs += 1
                if(k>i):
                    del array[i]
                else:
                    i+=1
                break
        if correctPairs == l - 1:
            i = 0
            break
    return array 

array1 = [6, 6, 6, 5]
array2 = [3, 9, 8, 4]
array3 = [8, 5, 2, 9, 5, 6, 3]
array4 = [1]
testCase8 = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]
print(insertionSort(testCase8))