#Not noted anything
#Complexities not tried
#Official solution seen : possibly not

def isMonotonic(array):
    isMonotonic = False
    isExpectedNonDecreasing = None
    isTrendPredicted = False
    i = 0
    while(i<len(array)-1):
        if array[i+1] == array[i]: i+= 1
        elif isTrendPredicted == False:
            if array[i+1]>array[i]:
                isExpectedNonDecreasing = True
                isTrendPredicted = True
                i += 1
            elif array[i+1]<array[i]:
                isExpectedNonDecreasing = False
                isTrendPredicted = True
                i+= 1
        else :
            if array[i+1] > array[i]:
                if isExpectedNonDecreasing == False:
                    return False
                else : i += 1
            elif array[i+1] < array[i]:
                if isExpectedNonDecreasing == True:
                    return False
                else:
                    i += 1
    return True 
