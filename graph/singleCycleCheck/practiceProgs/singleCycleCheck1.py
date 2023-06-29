def isSingleCycle(a):
    l = len(a)
    if (l<=1): return True
    i = 0
    noOfJumps = -1
    while(1):
        i = i % l
        if(i<0):    i = i + l        
        if(a[i]==1.5):  return False
        noOfJumps += 1       
        if(noOfJumps == l): return True 
        i = i % l
        if(i<0):    i = i + l
        iNext = i + a[i]
        a[i] = 1.5
        i = iNext 



a0 = []
a1 = [-2]
a2 = [1, 3]
a3 = [1, 2]
a4 = [1, 2, 4]
a5 = [2, -1, 2]
print(isSingleCycle(a5))