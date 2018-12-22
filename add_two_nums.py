#!/usr/bin/env python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        output = []
        while l1 or l2:
            if l1: 
                v1 = l1.val
            else:
                v1 = 0
            
            if l2: 
                v2 = l2.val
            else:
                v2 = 0
            
            v = (v1+v2) + carry
            
            if v//10:
                carry = 1
            else:
                carry = 0

            output.append(ListNode(v%10))
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry:    
            output.append(ListNode(carry))

        for i, j in zip(output, output[1:]):
            i.next = j
        output = output[0]

        return output


if __name__ == "__main__":
    l = [ListNode(2), ListNode(4), ListNode(3)]
    for i, j in zip(l, l[1:]):
        i.next = j
    l1 = l[0]
    
    l = [ListNode(5), ListNode(6), ListNode(4)]
    for i, j in zip(l, l[1:]):
        i.next = j
    l2 = l[0]

    output = Solution().addTwoNumbers(l1, l2)
    
    while output:
        print(output.val, end=" ")
        output = output.next
    print()
    






        



