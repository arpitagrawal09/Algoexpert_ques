def sortedSquaredArray(array):
    for i in range(len(array)):
        array[i]=abs(array[i])
    array.sort()
    for i in range(len(array)):
        array[i]=array[i]*array[i]
    return array
