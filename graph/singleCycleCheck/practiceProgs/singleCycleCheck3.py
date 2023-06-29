def isSingleCycle(a):
    l = len(a)
    if l <= 1 : return True
    i = 0
    nOJ = -1

    while(a[i]!=1.5):
        #print(nOJ)
        nOJ += 1
        i = updateValues(a, i)
    #print(nOJ)
    if (nOJ == l - 1) & (i==0): return True
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

a0 = []
a1 = [-2]
a2 = [1, 3]
a3 = [1, 2]
a4 = [1, 2, 4]
a5 = [2, -1, 2]
a6 = [1, 1, 1, 1, 2]
print(isSingleCycle(a6))