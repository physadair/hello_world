#!/usr/bin/env python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers_v0(self, l1, l2):
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
    
    def addTwoNumbers_v1(self, l1, l2):

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
        output = ListNode(0)
        currNode = output
        
        currNode.next = ListNode(v%10)
        v = v//10
        currNode = currNode.next
        while v:
            currNode.next = ListNode(v%10)
            v = v//10
            currNode = currNode.next

        
        return output.next

    #### addTwoNumbers_v2 ###
    def addTwoNumbers_v2(self, l1, l2):
        v1 = self.convertLinkedListToNumber(l1)
        v2 = self.convertLinkedListToNumber(l2)
        return self.convertNumberToLinkedList(v1+v2)

    def convertLinkedListToNumber(self, ll):
        v = 0
        currNode = ll
        i = 0
        while currNode:
            v += currNode.val*10**i
            i += 1
            currNode = currNode.next
        return v
    
    def convertNumberToLinkedList(self, v):
        l = []
        while True:
            l.append(v%10)
            v //= 10
            if not v: break

        return self.convertListToLinkedList(l);

    def convertListToLinkedList(self, l):
        currNode = ll = ListNode(None)
        for i in l:
            currNode.next = ListNode(i)
            currNode = currNode.next
        return ll.next

    def displayLinkedList(self, ll):
        currNode = ll
        while currNode:
            print(currNode.val, end=" ")
            currNode = currNode.next
        print()
    #### addTwoNumbers_v2 ###
    
    #### addTwoNumbers_v3 ###
    def addTwoNumbers_v3(self, l1, l2):
        l = currNode = ListNode(None)
        carry = v = i = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = (v1 + v2 + carry)%10
            carry = (v1 + v2)//10
            
            currNode.next = ListNode(v)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            currNode = currNode.next

        return l.next
    #### addTwoNumbers_v3 ###

    addTwoNumbers = addTwoNumbers_v3

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
