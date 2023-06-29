def twoNumberSum(array, targetSum):
    # Write your code here.
    numSet = set(array)
    pair = []
    
    for num1 in numSet:
        num2 = targetSum - num1
        if num2 in numSet:
            if(num1 != num2):
                pair = [num1, num2]
                break
    
    return pair
        