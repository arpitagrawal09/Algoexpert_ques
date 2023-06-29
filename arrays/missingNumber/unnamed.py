def missingNumbers(nums):
    # Write your code here.
    nums.sort()
    l = len(nums)
    tracker = [0, 0]
    for i in range(l):
        tracker.append(0)
    for i in range(0, l):
        val = nums[i]
        tracker[val-1] = 1
    missing = []
    for i in range(0, l+2):
        if(tracker[i]==0):
            missing.append(i+1)
    missing.sort()
    return missing

nums = [1, 2, 3, 6, 5, 7, 9]
print(missingNumbers(nums))
