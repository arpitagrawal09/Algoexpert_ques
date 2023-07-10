def squareSortedIntegers(array):

    for i in range(len(array)):
        array[i] = array[i] * array[i]

    array.sort()    
    return array

array1 = [1, 2, 5, 10]
array2 = []
array3 = [1]
array4 = [-9, -6]

print(squareSortedIntegers(array4))