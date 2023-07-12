array = [1, 4, 2, 7, 34]
sum = 35

nums = set(array)
#print(nums)

for num1 in nums:
    num2 = sum - num1
    if num2 in nums:
        print({num1, num2})
        break

nums = {3}
nums.add(4)
nums.add(5)
print(nums)

