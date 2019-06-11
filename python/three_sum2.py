#/usr/bin/env python

from itertools import combinations

class Solution(object):
    def three_sums(self, nums):
        nums = sorted(nums)
        result = [c for c in itertools.combinations(nums, 3) if not sum(c)]
        result = list(set(result))
        
        return result
