#!/usr/bin/env python

import numpy as np 

class Solution(object):
    def findKthLargest_v1(self, array, k):
        less = []
        greater = []
        if len(array) <= 1:
            return array[0]
        
        idx = len(array)//2
        pivot = array.pop(idx)
        for n in array:
            if n <= pivot:
                less.append(n)
            else:
                greater.append(n)
        if k <= len(greater):
            return self.findKthLargest(greater, k)
        elif k == len(greater)+1:
            return pivot
        else:
            return self.findKthLargest(less, k-len(greater)-1)

    def findKthLargest_v2(self, array, k):
        sorted_array = self.quickSort(array)
        return sorted_array[-k]

    findKthLargest = findKthLargest_v2

    def quickSort(self, array):
        less = []
        equal = []
        greater = []
        if len(array) <= 1:
            return array
        idx = len(array)//2
        pivot = array.pop(idx)
        equal.append(pivot)
        for n in array[1:]:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                equal.append(n)

        return self.quickSort(less) + equal + self.quickSort(greater)


if __name__ == "__main__":
    sol = Solution()
    list0 = list(np.random.randint(0, 100, size=50))
    print(sol.quickSort(list0))
    print(sol.findKthLargest_v2(list0, 10))
