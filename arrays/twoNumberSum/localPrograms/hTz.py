def twoSum(nums, target) :
    l = len(nums)
    pair = []
    numSet = {"initialise":"ignore"}
    for eleLeft in nums:
        eleComp = target - eleLeft
        if eleComp in numSet:
            pair = [eleLeft, eleComp]
            break
        else:
            numSet.update({eleLeft:True})
    return pair

nums = [2,7,11,15]
target = 9
pair = twoSum(nums, target)
print(pair)

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6