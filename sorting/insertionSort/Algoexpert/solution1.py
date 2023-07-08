#Submission at Algoexpert. Solution 1. I don't think its working

def insertionSort(array):
    l = len(array)
    noOfSwaps = -1
    while(noOfSwaps != 0):
        noOfSwaps = 0
        element = array[0]
        j = l - 1
        while(j>0):
            if element<array[j]:
                j -= 1
            else:
                array.insert(j+1, element)
                del array[0]
                noOfSwaps += 1
                break
    return array 
