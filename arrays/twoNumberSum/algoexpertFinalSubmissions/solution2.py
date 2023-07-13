#CORRECT. ALL TEST CASES PASSED
#Method 2 : Two Pointers 

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0 
    right = len(array)-1
    while(left<right):
        num1 = array[left]
        num2 = array[right]
        sum = num1 + num2 
        if sum==targetSum: return [num1, num2]
        elif sum>targetSum: right -= 1
        else: left += 1
    return []
        