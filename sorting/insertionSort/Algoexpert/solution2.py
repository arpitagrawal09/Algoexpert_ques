#Submission at Algoexpert. Solution 2. I don't think it's working

def insertionSort(array):
    l = len(array)
    nChanges = -1
    while(nChanges != 0):
        print(nChanges)
        if(array == [5, 2, 9, 5, 6, 3, 8]): print("Yes")
        nChanges = 0
        for i in range(l-1):
            print(i)
            hawk = array[i]
            j = l-1
            while((j>i)&(j<l)):
                #print(j)
                prey = array[j]
                if(hawk<prey):
                    j = j-1
                elif(hawk>prey):
                    del array[i]
                    array.insert(j, hawk)
                    nChange += 1
                    break
                else:
                    if(j != i+1):
                        del array[i]
                        array.insert(j, hawk)
    return array
                    