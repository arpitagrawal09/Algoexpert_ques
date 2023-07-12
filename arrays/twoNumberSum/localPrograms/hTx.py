def twoNumberSum(array, targetSum):
    l = len(array)
    array.sort()
    lP = 0
    rP = l-1
    pair = []
    while (lP<l-1) & (rP>0):
        eleLeft = array[lP]
        eleRight = array[rP]
        sumNow = eleLeft + eleRight
        if(sumNow == targetSum):
            pair = [eleLeft, eleRight]
            break
        elif( sumNow > targetSum):
            rP -= 1
        else:
            lP += 1
    return pair

"""nums1 = [2, 11, 15, 7]
target1 = 18
pair1 = twoNumberSum(nums1, target1)
print(pair1)"""

nums2 = [2, 11, 15, 7, 902, 29, 42, 37, 75]
target2 = 57
pair2 = twoNumberSum(nums2, target2)
print(pair2)