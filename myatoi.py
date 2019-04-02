#!/usr/bin/env python 
import re

class Solution:
    def myAtoi_v0(self, s: str) -> int:
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

    def myAtoi_v1(self, s: str) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        digits = "0123456789"
        signs = "+-"
        
        s = s.strip()
        i = 0
        num = 0
        factor = 1
        for i in range(len(s)):
            if i == 0 and s[i] in signs:
                factor = int(s[0] + "1")
            elif s[i] in digits:
                num = 10*num + int(s[i])
            else:
                break 
        
        num *= factor
        if num < MIN_INT:
            return MIN_INT
        elif num > MAX_INT:
            return MAX_INT
        else:
            return num

    myAtoi = myAtoi_v1




if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("   +-42 "))
    print(sol.myAtoi("   -42 "))
