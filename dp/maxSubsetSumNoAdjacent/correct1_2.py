#Attempt to revise one of the methods. Basic aim is to come up with the level of the official solution myself
#Time : 10 minutes to write the code
#Time : 33 mins of debugging.
#Bug1)    related to the second element 
#Bug2)    typing error between i and 1
#Learning)    Debugging at online compiler of Algoexpert 

def maxSubsetSumNoAdjacent(array):
    l = len(array)
    #if l != 3 : return -1
    #print(array)
    #print(l)
    if l == 0: return 0
    if l == 1: return array[0]
    maxSumArr = [array[0], max(array[0], array[1])]
    #print(maxSumArr)
    for i in range(2, l):
        numSecondLast = maxSumArr[i-2]
        numLast = maxSumArr[i-1]
        #print(numLast)
        num = array[i]
        #print(numSecondLast, numLast, num)

        sum1 = numSecondLast + num
        sum2 = numLast
        #print(sum1, sum2)
        maxSum = max(sum1, sum2)
        #print(maxSum)
        maxSumArr.append(maxSum)

    #print(maxSumArr)
    return maxSumArr[l-1]





