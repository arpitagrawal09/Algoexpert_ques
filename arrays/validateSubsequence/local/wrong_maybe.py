def isValidSubsequence(array, subseq):
    i = 0
    j = 0
    while((i<len(array))&(j<len(subseq))):
        nowArr = array[i]
        nowSS = subseq[j]
        if(nowArr < nowSS): i+=1
        elif(nowArr == nowSS):
            if(j==len(subseq)-1): return True
            else:
                i+=1
                j+=1
        else: j+=1
    return False

