def twoNumberSum(array, targetSum):
    array.sort()
    iLeft = 0 
    iRight = len(array)-1
    while(iLeft<iRight):
        left = array[iLeft]
        right = array[iRight]
        sum = left + right 
        if sum==targetSum: return [left, right]
        elif sum>targetSum: iRight -= 1
        else: iLeft += 1
    return []
        