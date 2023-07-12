def twoNumberSum(arr, target):
    hT = {arr[0]}
    for num in arr:
        complement = target - num
        if complement in arr:
            return [num, complement]

arr1 = [1,2,3,4,5]
target = 7
result = twoNumberSum(arr1, target)
print(result)
