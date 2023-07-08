def twoNumberSum(arr, target):
    setNums = set(arr)
    for num in arr:
        complement = target - num
        if complement in setNums:
            return num
        else:
            setNums.update({complement})
    return -1

arr1 = [1,2,3,4,5]
target = 7
result = twoNumberSum(arr1, target)
print(result)
