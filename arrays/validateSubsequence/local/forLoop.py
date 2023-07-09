def isValidSubsequence(array, sequence):
    lSeq = len(sequence)
    lArr = len(array)
    arrIdx = 0
    seqIdx = 0
    for seqIdx in range(lSeq):
        while(arrIdx < lArr):
            if(array[arrIdx]==sequence[seqIdx]):
                break
        arrIdx += 1
    return seqIdx == lSeq