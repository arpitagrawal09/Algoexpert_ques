def twoNumberSum(array, targetSum):
    array.sort()
    l = len(array)
    left = 0
    right = l - 1
    while(left!=right):
        num1 = array[left]
        num2 = array[right]
        sum = num1 + num2 
        if (sum==targetSum):
            return [num1, num2]
        elif(sum > targetSum): right -= 1
        else: left += 1
    return []

numbers1 = []
targetSum1 = 0

numbers2 = [-92]
targetSum2 = [-2]

numbers3 = [-8, 2]
targetSum3 = -6

numbers4 = [2, -8]
targetSum4 = -26

numbers5 = [2, -8, 35]
targetSum5 = -26

numbers6 = [-2, -8, 35]
targetSum6 = 33

pair = twoNumberSum(numbers6, targetSum6)
print(pair)