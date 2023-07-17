#Accepted at algoexpert. Time Complexity I could do, but not written here
#Author : Arpit Agrawal     Date : 16/07
#1st ques of dynamic programming at Algoexpert 
#Written in two sytles
#Took the algorithm hint from Microsoft Bing. Not seen the official solution yet

def maxSubsetSumNoAdjacent(array):
    if len(array)==0: return 0
    if len(array)==1: return array[0]
    if len(array)==2: return max(array[0], array[1])

    #Get first and second entries of given array
    num0 = array[0]
    num1 = array[1]
    #Get first and second entreis of the masSubsetArray
    maxSum0 = num0
    maxSum1 = max(num0, num1)
    #Set these 2 entries 
    maxSumArray = [maxSum0, maxSum1]
    #maxSumArray = [array[0], max(array[0], array[1])]

    #Get the max value upto the given index 
    for i in range(2, len(array)):
        thisNum = array[i]
        lastNum = maxSumArray[i-1]
        secondLastNum = maxSumArray[i-2]
        
        #find out the two possible sums
        sumA = lastNum
        sumB = secondLastNum + thisNum
        #find out one of these two sums
        thisMaxSum = max(sumA, sumB)
        #thisMaxSum = max(array[i-2]+array[i], array[i-1])

        #append this maxSum
        maxSumArray.append(thisMaxSum)

    #The last entry gives the max subset sum 
    return maxSumArray[len(array)-1]
    


