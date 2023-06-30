#Submission at Algoexpert. Solution 1. Accepted 
def productSum(array):
    return getProSum(array, 1)

def getProSum(array, depth):
    proSum = 0
    for element in array:
        if type(element)==list:
            proSum += getProSum(element, depth+1)
        else: proSum += element 
    return proSum * depth
