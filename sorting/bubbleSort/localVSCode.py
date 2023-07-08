#Tried at Local VSCode. Seems to be exactly same as the Algoexpert solution. Not sure if it works or not
def bubbleSort(array):

    l = len(array)
    if(l>1):
        totalPairs = l - 1
    else: totalPairs = 0

    nPairsSorted = 0 
    while(nPairsSorted != totalPairs):
        nPairsSorted = 0
        for i in range(l-1):
            elementNow = array[i]
            elementNext = array[i+1]
            if(elementNow>elementNext):
                array[i] = elementNext
                array[i+1] = elementNow
            else:
                nPairsSorted += 1

    return array

array1 = [3, 2, 1]
array2 = []
array3 = [-73]
array4 = [6532, 5,256, 204, -0.4682, -32, -5.234, -738.26851]
print(bubbleSort(array4))
            