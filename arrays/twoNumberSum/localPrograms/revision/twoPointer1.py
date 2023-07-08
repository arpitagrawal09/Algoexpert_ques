def twoNumberSum(arr, target):
    l = len(arr)
    i = 0
    j = l-1
    while((i<l)&(j>0)&(i<j)):
        num1 = arr[i]
        num2 = arr[j]
        sum = num1 + num2
        if sum==target:
            return [i, j]
        elif sum>target:
            j-=1
        else: i+=1
    return [-1, -1]

arr1 = [1,2,3,4,5]
target = 7
result = twoNumberSum(arr1, target)
print(result)

