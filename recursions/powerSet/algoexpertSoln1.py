#Submission at algoexpert. Solution 1. Accepted 
def powerset(array):
    return getPowerset(array)

def getPowerset(array):
    if len(array) == 0: return [[]]
    if len(array) == 1: return [[], array]
    thisSet = [[]]
    for i in range(len(array)):
        tempArr = array[0:i] + array[i+1:]
        thisSet += getPowerset(tempArr)
    thisSet += [array]
    uniqueSet = []
    [uniqueSet.append(set) for set in thisSet if set not in uniqueSet]
    return uniqueSet