def binarySearch(array, target):
    # Write your code here.
    l = len(array)
    #iMid = l//2
    iLeft = 0
    iRight = l-1
    while(iLeft<=iRight):
        iMid = (iLeft + iRight)//2
        ele = array[iMid]
        if(target==ele):
            return iMid
        elif(target<ele):
            iRight = iMid - 1
        else:
            iLeft = iMid + 1
    return -1

array = [0, 1, 2, 3, 4]
print(binarySearch(array, 4))
