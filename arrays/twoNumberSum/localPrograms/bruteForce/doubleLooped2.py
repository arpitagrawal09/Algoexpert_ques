#Correct. Should be passing all the test cases at algoexpert

def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        num1 = array[i]
        for j in range(i+1, len(array)):
            if(num1+array[j]==targetSum):
                return [num1, array[j]]
    return []

print(twoNumberSum([1, 2, 3], 4))