def isValidSubsequence(array, sequence):
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
            else:
                i += 1
    if j == lSeq: 
        return True
    return False
