#!/usr/bin/env python 
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        d = re.match(" *[-+]?\d+", s)
        d = 0 if d is None else int(d.group(0))
        
        if d < MIN_INT:
            return MIN_INT
        elif d > MAX_INT:
            return MAX_INT
        else:
            return d

if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("   +-42 "))
    print(sol.myAtoi("   -42 "))
