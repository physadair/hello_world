#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};


class Solution {
public:
    ListNode* addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *l = new ListNode(0);
        ListNode *curr = l;
        int carry = 0;
        int v1 = 0;
        int v2 = 0;
        int v = 0;
        while (l1 != NULL || l2 != NULL || carry != 0) 
        {
            v1 = (l1 != NULL) ? l1->val : 0;
            v2 = (l2 != NULL) ? l2->val : 0;
            v = (v1 + v2 + carry)%10;
            carry = (v1 + v2 + carry)/10;
            curr->next = new ListNode(v);
            
            curr = curr->next;
            l1 = (l1 != NULL) ? l1->next : NULL;
            l2 = (l2 != NULL) ? l2->next : NULL;
        }
        return l->next;
    
    }
};
