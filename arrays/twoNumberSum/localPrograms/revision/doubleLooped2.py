def twoNumberSum(arr, target):
    for i in range(len(arr)-1):
        num1 = arr[i]
        for j in range(i+1, len(arr)):
            if(num1+arr[j]==target):
                return [num1, arr[j]]
    return []

print(twoNumberSum([1, 2, 3], 4))