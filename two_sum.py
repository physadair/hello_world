#!/usr/bin/env python 

class Solution(object):
    def twoSum(self, nums, target):
        nums_map = dict()
        for idx, num in enumerate(nums):
            if num in nums_map.keys():
                return [nums_map[num], idx]
            else:
                nums_map[target-num] = idx

