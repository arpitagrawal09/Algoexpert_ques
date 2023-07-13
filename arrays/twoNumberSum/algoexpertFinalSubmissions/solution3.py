#CORRECT. ALL TEST CASES PASSED
#Method 3 : Hash Table lookup

def twoNumberSum(array, targetSum):
    numTable = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in numTable:
            ans = [num, potentialMatch]
            ans.sort()
            return ans
        else:
            numTable[num]=True
    return []

    