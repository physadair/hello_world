#!/usr/bin/env python 

class Solution(object):
    def __init__(self):
        self.memory = {}
    def isMatch(self, s, p):
        if not p:
            return not s;

        if (s, p) in self.memory:
            return self.memory[s, p]

        first_match = bool(s) and p[0] in (s[0], '.')
        if len(p)>=2 and p[1] == '*':
            self.memory[s, p] = self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            self.memory[s, p] = first_match and self.isMatch(s[1:], p[1:])
        return self.memory[s, p]
