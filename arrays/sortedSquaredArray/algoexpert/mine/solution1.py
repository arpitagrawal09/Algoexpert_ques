def sortedSquaredArray(array):
    # Write your code here.
    for i in range(len(array)):
        array[i]= array[i]*array[i]
    array.sort()
    return array