def twoNumberSum(array, targetSum):
    # Write your code here.
    ans = []
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            int1 = array[i]
            int2 = array[j]
            if(int1 + int2 == targetSum):
                ans = [int1, int2]
                return ans
    return ans
