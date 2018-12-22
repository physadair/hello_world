#!/usr/bin/env python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        output = ListNode(0)
        currNode = output
        while l1 or l2 or carry: 
            if l1: 
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            
            if l2: 
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            
            v = (v1+v2) + carry
            carry = 1 if v//10 else 0

            currNode.next = ListNode(v%10)
            currNode = currNode.next
        
        return output.next
    
    def addTwoNumbers_v2(self, l1, l2):

        v1 = 0
        i = 0
        while l1:
            v1 += l1.val*(10**i)
            i += 1
            l1 = l1.next
        
        v2 = 0
        j = 0
        while l2:
            v2 += l2.val*(10**j)
            j += 1
            l2 = l2.next
        
        v = v1 + v2
        output = []
        
        output.append(ListNode(v%10))
        v = v//10
        while v:
            output.append(ListNode(v%10))
            v = v//10
        
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
    






        



