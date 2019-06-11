#!/usr/bin/env python

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        string = []
        longest_string = []
        for c in s:
                if c in string:
                    if len(longest_string) < len(string):
                        longest_string = string 
                    string = string[string.index(c)+1:]
                string.append(c)
        else:
            if len(longest_string) < len(string):
                longest_string = string 
        return len(longest_string)

    def lengthOfLongestSubstring_v2(self, s):
        temp_str = ""
        i = 0
        max_len = 0
        for j in range(len(s)):
            if s[j] in temp_str:
                if len(temp_str) > max_len:
                    max_len = len(temp_str)
                i = s.find(s[j], i, len(s)) + 1
            temp_str = s[i:j+1]
        if len(temp_str) > max_len:
            max_len = len(temp_str)

        return max_len

    lengthOfLongestSubstring = lengthOfLongestSubstring_v2

                





print(Solution().lengthOfLongestSubstring("abcdefg"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring(" "))
print(Solution().lengthOfLongestSubstring("dvdf"))

