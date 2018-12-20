#/usr/bin/env python

class Solution(object):
    def countBits(self, num):
        output = []
        for i in range(num+1):
            count = sum(int(i) for i in bin(i)[2:])
            output.append(count)
        
        return output

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(50))
