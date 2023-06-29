def twoNumberSum(array, targetSum):
    # Write your code here.
    l = len(array)
    numHT = {"initialize":"ignore"}
    for num in array:
        keyList = numHT.keys()
        eleLeft = num
        eleRight = targetSum - eleLeft
        if (eleRight in numHT):
            if (numHT[eleRight]==True):
                return[eleLeft, eleRight]
        else:
            numHT.update({eleLeft : True})

    return []