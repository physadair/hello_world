#!/usr/bin/env python

class Solution(object):
    def convert(self, s, numRows):
        output = [[]*numRows for _ in range(numRows)]
        row = self.zigzag(numRows)
        for c, r in zip(s, row):
            output[r].append(c)
        return "".join(["".join(line) for line in output])

    def zigzag(self, numRows):
        while True:
            for i in range(numRows):
                yield i
            for i in range(numRows-2, 0, -1):
                yield i

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
