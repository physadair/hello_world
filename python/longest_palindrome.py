#!/usr/bin/env python 

class Solution(object):
    def longestPalindrome(self, s):
        pass
        

    def isPalindrome(self, s):
        n = len(s)
        for i in range(n//2):
            print(i, n-i-1, s[i], s[n-i-1])
            if s[i] != s[n-i-1]: return False
        return True

if __name__ == "__main__":
    s1 = "abcdedcba"
    s2 = "abcdefg"

    print(Solution().isPalindrome(s2))
    print(Solution().isPalindrome(s1))

