#!/usr/bin/env python 

class Solution(object):
    def longestPalindrome(self, s):
        max_palindrome = ""
        for i in range(len(s)):
            # odd 
            for t in range(2):
                j = 0
                while i+j+t<len(s) and i-j>=0:
                    if (s[i-j] == s[i+j+t]):
                        if len(s[i-j:i+j+t+1]) > len(max_palindrome):
                            max_palindrome = s[i-j:i+j+t+1]
                    else:
                        break
                    j += 1
        
        return max_palindrome

if __name__ == "__main__":
    print(Solution().longestPalindrome('adddaabcdefghgfedcbazz'))
    print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('c'))
                
