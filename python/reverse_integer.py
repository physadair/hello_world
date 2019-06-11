#!/usr/bin/env python

class Solution:
    def reverse_v0(self, x: int) -> int:
	flag = True if x < 0 else False
	x = abs(x)
	r = 0
        while True:
            if not x: break
            r = r*10 + x%10
            x //= 10

	r = -r if flag else r
	if r < -2**31 or r > (2**31-1):
	    r = 0
        
        return r

    def reverse_v1(self, x: int) -> int:
        MAXINT = 2**31
        flag = True if x < 0 else False
        x = abs(x)
        r = 0
        while x:
            if r > MAXINT/10: return 0
            r = r*10 + x%10
            x //= 10

        r = -r if flag else r
        return r

    reverse = reverse_v1


        

