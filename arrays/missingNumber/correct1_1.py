def missingNumbers(nums):
    # Write your code here.
    nums.sort()
    lN = len(nums)
    lT = lN + 2
    tracker = [-1, -1]
    for i in range(lN):
        tracker.append(-1)
    for i in range(0, lN):
        val = nums[i]
        tracker[val-1] = 1
    missing = []
    for i in range(0, lT):
        if(tracker[i]==-1):
            missing.append(i+1)
    missing.sort()
    return missing