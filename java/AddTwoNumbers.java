public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2)
    {
        ListNode l = new ListNode(0);
        ListNode curr = l;
        int carry = 0;
        int v1 = 0;
        int v2 = 0;
        int v = 0;
        while (l1 != null || l2 != null || carry != 0) 
        {
            v1 = (l1 != null) ? l1.val : 0;
            v2 = (l2 != null) ? l2.val : 0;
            v = (v1 + v2 + carry)%10;
            carry = (v1 + v2 + carry)/10;
            curr.next = new ListNode(v);
            
            curr = curr.next;
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }
        return l.next;
    }
}
