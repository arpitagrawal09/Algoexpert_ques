def bubbleSort(array):
    # Write your code here.
    l = len(array)
    if(l>1): totalPairs = l - 1
    else: totalPairs = 0

    nPairsSorted = 0
    while(nPairsSorted != totalPairs):
        nPairsSorted = 0
        for i in range(l-1):
            ele1 = array[i]
            ele2 = array[i+1]
            if(ele1>ele2):
                array[i]=ele2
                array[i+1]=ele1
            else:
                nPairsSorted += 1
    return array
