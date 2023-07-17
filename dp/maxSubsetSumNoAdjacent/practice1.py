#Attempt date - somewhere before July 2023
#No notes taken. No idea if it is correct or not

def maxSubsetSumNoAdjacent(array):
    sumFromFirst = 0
    sumFromSecond = 0

    for i in range(0, len(array)):
        if i%2 == 0: sumFromFirst += array[i]
        else: sumFromSecond += array[i]
    return max(sumFromFirst, sumFromSecond)