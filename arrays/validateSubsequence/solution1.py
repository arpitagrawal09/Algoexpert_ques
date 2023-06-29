def isValidSubsequence(array, sequence):
    # Write your code here.
    isSubsequence = False 
    i = 0
    j = 0
    lenA = len(array)
    lenS = len(sequence)
    while((i<lenA)&(j<lenS)):
            int1 = array[i]
            int2 = sequence[j]
            if(int1==int2):
                i+=1
                j+=1
                if(j==lenS):
                    isSubsequence = True
                    break
            else:
                i+=1

    return isSubsequence 


