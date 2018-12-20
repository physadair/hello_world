#!/usr/bin/env python 

class Solution(object):
    def hammingWeight(self, num):
        if num//2 == 0:
            return num%2
        else:
            return num%2 + self.hammingWeight(num//2)
