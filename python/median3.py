#!/usr/bin/env python 

class Solution(object):
    def findMedianSortedArrays(nums1, nums2):
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
    

