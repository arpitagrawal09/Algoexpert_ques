def isSubSequence(array, sequence):
    i = 0
    j = 0
    lArray = len(array)
    lSeq = len(sequence)
    while((i<lArray)&(j<lSeq)):
            numArray = array[i]
            numSeq = sequence[j]
            if numArray == numSeq:
                i += 1
                j += 1
                a = 1
            else:
                i += 1
                a = 1
    if j == lSeq: 
        return True
    return False

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 23, 6, -1, 8, 10]
print(isSubSequence(array, sequence))