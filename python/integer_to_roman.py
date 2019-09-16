#!/usr/bin/env python

class Solution(object):
    def intToRoman(self, num: int) -> str:
        integers = [1000, 500, 100, 50, 10, 5, 1]
        romans = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        str_ = ''
        
        q = num // integers[0]
        num = num % integers[0]
        str_ += romans[0]*q
        for i in range(1, len(integers), 2):
            q = num // integers[i]
            r = (num % integers[i]) // integers[i+1]
            if q==1 and r==4:
                str_ += (romans[i+1] + romans[i-1])
            elif q==0 and r==4:
                str_ += (romans[i+1] + romans[i])
            else:
                str_ += romans[i]*q + romans[i+1]*r
            num %= integers[i+1]

        return str_



print(Solution().intToRoman(1994))



