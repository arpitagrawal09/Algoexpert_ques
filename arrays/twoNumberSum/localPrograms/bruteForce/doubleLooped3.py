#Correct. Passed all test cases in algoexpert. Exactly same as solution 1
#Keywords - twoSum, Sorted, Non empty, at most one such pair, distinct
#Method one, two coupled loop - finding all pairs and checking the equality for each of the pairs  

def twoNumberSum(array, target):
    l = len(array)
    for i in range(l):
        num1 = array[i]
        for j in range(i+1, l):
            num2 = array[j]
            if(num1+num2==target):
                return [i, j]
    return []