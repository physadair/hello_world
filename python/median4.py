#!/usr/bin/env python 

class Solution(object):
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
        else:
            return self.getkth(nums1[i:], nums2[:], k-i)

    def findMedianSortedArrays_v5(self, nums1, nums2):
        l = (len(nums1) + len(nums2) + 1)//2 
        r = (len(nums1) + len(nums2) + 2)//2

        
        return (self.getkth(nums1, nums2, l) + self.getkth(nums1, nums2, r))/2.

    findMedianSortedArrays = findMedianSortedArrays_v5


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays_v5([1, 2, 3, 4], [5, 6, 7]))
    print(Solution().findMedianSortedArrays_v5([1, 2, 3, 4], [5, 5, 6, 7]))
    print(Solution().findMedianSortedArrays_v5([1, 2, 3, 4, 4, 5], [5, 6, 7]))
    print(Solution().findMedianSortedArrays_v5([1, 2], [1, 2]))

