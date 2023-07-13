def twoNumberSum(array, target):
    iLeft = 0 
    iRight = len(array)-1
    while(iLeft<iRight):
        left = array[iLeft]
        right = array[iRight]
        sum = left + right 
        if sum==target: return [left, right]
        elif sum>target: iRight -= 1
        else: iLeft += 1
    return []

