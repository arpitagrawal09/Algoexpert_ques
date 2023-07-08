#Submission at Algoexeprt. Solution 3. I don't think its working

def insertionSort(array):
    l = len(array)
    correctPairs = 0
    i = 0
    while(i < l):
        e = array[i]
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