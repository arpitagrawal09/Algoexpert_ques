def bubbleSort(array):
    i = 0
    changedPairs = -1
    while((changedPairs!=0)):
        i=0
        changedPairs = 0
        while(i<len(array)-1):
            first = array[i]
            second = array[i+1]
            if(first>=second):
                array[i+1]=first
                array[i]=second
                changedPairs+=1
            i+=1
    return array

array1 = [2,1,3,1]
sortedArray = bubbleSort(array1)
print(sortedArray)