#CORRECT. ALL TEST CASES PASSED
#Method one, two coupled loop - finding all pairs and checking the equality for each of the pairs  

def twoNumberSum(array, targetSum):
    l = len(array)
    for i in range(l):
        num1 = array[i]
        for j in range(i+1, l):
            num2 = array[j]
            if(num1+num2==targetSum):
                return [num1, num2]
    return []