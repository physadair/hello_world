#!/usr/bin/env python 

import copy
import timeit
import numpy as np

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + num2)

        if len(nums)%2:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2-1] + nums[len(nums)//2])/2.

    def findMedianSortedArrays_v2(self, nums1, nums2):
        nums = self.merge(nums1, nums2)
        
        if len(nums)%2:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2-1] + nums[len(nums)//2])/2.

    def merge(self, nums1, nums2):
        nums1 = copy.deepcopy(nums1)
        nums2 = copy.deepcopy(nums2)
        nums = []
        while nums1 and nums2:
            if nums1 < nums2:
                nums.append(nums1.pop(0))
            else:
                nums.append(nums2.pop(0))
        nums.extend(nums1 if nums1 else nums2)

        return nums

    def findMedianSortedArrays_v3(self, nums1, nums2):
        nums = self.merge_sort(nums1+nums2)
        
        if len(nums)%2:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2-1] + nums[len(nums)//2])/2.

    def merge_sort(self, nums):
        nums = copy.deepcopy(nums)
        if len(nums) < 2:
            return nums
        else:
            mid = len(nums)//2
            left = self.merge_sort(nums[:mid])
            right = self.merge_sort(nums[mid:])

        result = []
        while left and right:
            if left<right:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left if left else right)

        return result
    
    def findMedianSortedArrays_v4(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m>n:
            m, n = n, m
            nums1, nums2 = nums2, nums1
    
        max_of_left = min_of_right = 0
        i = m//2
        while True:
            j = (m+n)//2 - i
            if (i<m-1) and (nums1[i]<nums2[j-1]):
                i += 1
            elif (i>0) and (nums2[j]<nums1[i-1]):
                i -= 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums2[j-1], nums1[i-1])
     
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums2[j], nums1[i])
        
                if (m+n)%2:
                    return min_of_right
                else:
                    return (max_of_left+min_of_right)/2.
    
    def getkth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m>n:
            return self.getkth(nums2, nums1, k)

        if m == 0:
            return nums2[k-1]

        if k == 1:
            return min(nums1[0], nums2[0])

        i = min(m, k//2)
        j = min(n, k//2)

        if nums1[i-1]>nums2[j-1]:
            return self.getkth(nums1[:], nums2[j:], k-j)
        elif nums1[i-1]<nums2[j-1]:
            return self.getkth(nums1[i:], nums2[:], k-i)
        else: 
            return nums1[i-1]

    def findMedianSortedArrays_v5(self, nums1, nums2):
        l = (len(nums1) + len(nums2) + 1)//2 
        r = (len(nums1) + len(nums2) + 2)//2
        
        return (self.getkth(nums1, nums2, l) + self.getkth(nums1, nums2, r))/2.



    findMedianSortedArrays = findMedianSortedArrays_v3

if __name__ == "__main__":
    nums1 = sorted(np.random.randint(0, 100, 50))
    nums2 = sorted(np.random.randint(0, 100, 50))
    
    
    #print(timeit.timeit("Solution().findMedianSortedArrays_v2(nums1, nums2)", "from __main__ import Solution, nums1, nums2"))
    print(timeit.timeit("Solution().findMedianSortedArrays_v4(nums1, nums2)", "from __main__ import Solution, nums1, nums2"))
    print(timeit.timeit("Solution().findMedianSortedArrays_v5(nums1, nums2)", "from __main__ import Solution, nums1, nums2"))

