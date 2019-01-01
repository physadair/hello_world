#!/usr/bin/env python

class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[-1]
        closest_dist = abs(result-target)
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                temp = nums[i]+nums[l]+nums[r]
                dist = abs(temp-target)  
                if dist<closest_dist:
                    result = temp
                    closest_dist = dist
                if temp>target: 
                    r -= 1
                elif temp<target:
                    l += 1
                else: 
                    r -= 1
                    l += 1
                    if nums[r] == nums[l]: break
        
        return result

nums = [0, 2, 1, -3]
target  = 1
print(Solution().threeSumClosest(nums, target))
