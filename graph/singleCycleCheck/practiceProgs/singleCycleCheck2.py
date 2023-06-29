def isSingleCycle(a):
    l = len(a)
    i = 0
    nOJ = -1 

    while(nOJ<l):
        if(a[i]==1.5): return False
        iNext = i + a[i]
        a[i] = 1.5 
        i = iNext
        i = i % l 
        if i < 0 : i += l
        nOJ += 1
    return True

a0 = []
a1 = [-2]
a2 = [1, 3]
a3 = [1, 2]
a4 = [1, 2, 4]
a5 = [2, -1, 2]
print(isSingleCycle(a2))