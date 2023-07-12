class Solution:
    def twoSum(self, nums, target) : 
        l = len(nums)
        i = -1
        j = -1
        for i in range(l):
            for j in range(l):
                if(i!=j):
                    sum = nums[i]+nums[j]
                    if(sum==target):
                        return [i,j]
                    
nums = [2,7,11,15]
target = 9
ans = [0, 1]

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6