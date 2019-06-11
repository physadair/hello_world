#!/usr/bin/env python 

class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        vowels = "aeiouAEIOU"
        i, j = 0, len(s)-1
        while i<j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
        return "".join(s)

if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))
