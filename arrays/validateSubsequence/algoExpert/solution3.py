def isValidSubsequence(array, sequence):
    idArray = 0
    idSeq = 0
    while((idArray<len(array))&(idSeq<len(sequence))):
        if(array[idArray]==sequence[idSeq]): idSeq += 1
        idArray += 1
    return idSeq == len(array)