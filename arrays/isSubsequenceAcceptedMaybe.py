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

"""array = [1, 2, 3, 4]
subseq = [2, 4]
isSS = isValidSubsequence(array, subseq)
print(isSS)"""

"""array = [1, 2, 3, 4]
subseq = [2, 4, 5]
isSS = isValidSubsequence(array, subseq)
print(isSS)"""

"""array = [29, 81, 3, 42, 39]
subseq = [81, 42]
isSS = isValidSubsequence(array, subseq)
print(isSS)"""

"""array = [1]
subseq = [1]
isSS = isValidSubsequence(array, subseq)
print(isSS)"""

"""array = [0]
subseq = [1]
isSS = isValidSubsequence(array, subseq)
print(isSS)"""

"""array = []
subseq = [1]
isSS = isValidSubsequence(array, subseq)
print(isSS)"""

"""array = [1]
subseq = []
isSS = isValidSubsequence(array, subseq)
print(isSS)"""

array = []
subseq = []
isSS = isValidSubsequence(array, subseq)
print(isSS)