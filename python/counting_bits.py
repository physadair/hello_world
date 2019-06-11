#/usr/bin/env python

class Solution(object):
    def countBits(self, num):
        output = []
        for i in range(num+1):
            count = sum(int(i) for i in bin(i)[2:])
            output.append(count)
        
        return output

    def countBits_v2(self, num):
        result = [0]
        for i in range(1, num+1):
            result.append(i%2 + result[i//2])

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(50))
