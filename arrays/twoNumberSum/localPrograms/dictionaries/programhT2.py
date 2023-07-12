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

# Test Case 1
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
output = twoNumberSum(array, targetSum)
print(output)  # Expected: [-1, 11]

# Test Case 2
array = [4, 6]
targetSum = 10
output = twoNumberSum(array, targetSum)
print(output)  # Expected: []

# Test Case 3
array = [4, 6, 1]
targetSum = 5
output = twoNumberSum(array, targetSum)
print(output)  # Expected: [1, 4]

# Test Case 4
array = [4, 6, 1, -3]
targetSum = 3
output = twoNumberSum(array, targetSum)
print(output)  # Expected: [6, -3]

# Test Case 5
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
targetSum = 17
output = twoNumberSum(array, targetSum)
print(output)  # Expected: [8, 9]

# Test Case 6
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
targetSum = 18
output = twoNumberSum(array, targetSum)
print(output)  # Expected: [3, 15]

# Test Case 7
array = [-7, -5, -3, -1, 0, 1, 3, 5, 7]
targetSum = -5
output = twoNumberSum(array, targetSum)
print(output)  # Expected: [-5, 0]

# Test Case 8
array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
targetSum = 163
output = twoNumberSum(array, targetSum)
print(output)  # Expected: [12, 151]

# Test Case 9
array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
targetSum = 164
output = twoNumberSum(array, targetSum)
print(output)  # Expected: []

# Test Case 10
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 15
output = twoNumberSum(array, targetSum)
print(output)  # Expected: []

# Test Case 11
array = [14]
targetSum = 15
output = twoNumberSum(array, targetSum)
print(output)  # Expected: []

# Test Case 12
array = [15]
targetSum = 15
output = twoNumberSum(array, targetSum)
print(output)  # Expected: []