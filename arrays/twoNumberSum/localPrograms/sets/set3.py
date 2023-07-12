def twoNumberSum(array, target):
    numbers = set(array)
    for num1 in numbers:
        potentiolMatch = target - num1
        if potentiolMatch in numbers:
            return [num1, potentiolMatch]
    return []

nums1 = []
target1 = 2

nums2 = [1]
target2 = 1

nums3 = [-3, 7]
target3 = 10

nums4 = [7, 3]
target4 = 10

nums5 = [3, 7, -4, 81, -32, 18]
target5 = 49

nums6 = [3, 7, -4, 81, -32, 18]
target6 = 48

pairArray = twoNumberSum(nums6, target6)
print(pairArray)