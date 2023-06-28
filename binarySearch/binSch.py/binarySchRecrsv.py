def getIndex(array, lo, hi, key):
    l = len(array)
    iMid = (hi + lo)//2
    eleMid = array[iMid]
    if(eleMid==key):
        return iMid
    elif(key<eleMid):
        return getIndex(array, lo, iMid-1, key)
    else:
        return getIndex(array, iMid+1 , hi, key)
    
array2=[0, 1, 2, 3, 4, 5]
array1=[0, 1, 2, 3, 4]
print(getIndex(array2, 0, 5, 5))