#Passed all test cases at algoexpert - Yes/No
#Should be the last attempt 

def twoNumberSum(array, targetSum):
    dict = {}
    for num1 in array:
        potentiolMatch = targetSum - num1
        if potentiolMatch in dict: 
            return [num1, potentiolMatch]
        else:
            dict[num1] = True
    return []