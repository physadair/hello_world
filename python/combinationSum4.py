#!/usr/bin/env python

class Solution(object):
    def combinationSum4(self, nums, target):
        if target == 0:
            return 1
        elif target < 0:
            return 0
        result = 0
        for num in nums:
            result += self.combinationSum4(nums, target-num)

        return result

    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        nums = sorted(nums)
        
        for i in range(target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]

        return dp[target]



if __name__ == "__main__":
    print(Solution().combinationSum4([1, 2, 3], 4))
