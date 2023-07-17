#Better due to the complexity?
#Time : Must have been 20 mins 
def maxSubsetSumNoAdjacent(array):
    l = len(array)
    if not(l): return 0
    first = array[0]
    if l == 1: return first
    second = max(first, array[1])
    if l == 2: return second 
    lastNum = second
    secondLastNum = first
    for i in range(2, l):
        thisNum = array[i]
        sumChoice1 = secondLastNum + thisNum
        sumChoice2 = lastNum
        sumChosen = max(sumChoice1, sumChoice2)
        secondLastNum = lastNum
        lastNum = sumChosen
    return sumChosen