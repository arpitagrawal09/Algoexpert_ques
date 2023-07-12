def twoNumberSum(array, targetSum):
    # Write your code here.
    l = len(array)
    numHT = {"initialize":"ignore"}
    for num in array:
        keyList = numHT.keys()
        print(keyList)
        eleLeft = num
        eleRight = targetSum - eleLeft
        if(eleRight in numHT):
            if(numHT[eleRight]==True):
              return [eleLeft, eleRight]
        else:
            numHT.update({eleLeft : True})

nums = [2, 11, 15, 7]
target = 18
pair = twoNumberSum(nums, target)
print(pair)
