def hasSingleCycle(array):
    l = len(array)
    if l <= 1 : return True
    i = 0
    nOJ = -1

    while(array[i]!=1.5):
        print(nOJ)
        nOJ += 1
        i = updateValues(array, i)
    #if nOJ == l - 1
    if ((nOJ == l - 1) & (i==0)): return True
    return False

def updateValues(a, i):
    iNext = i + a[i]
    a[i] = 1.5 
    i = iNext
    i = normaliseIndex(a, i)
    return i 

def normaliseIndex(a, i):
    l = len(a)
    i = i % l
    if i <0 : i += l
    return i 
