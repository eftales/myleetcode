/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null){
            return null;
        }

        int lenA = getListLen(headA);
        int lenB = getListLen(headB);
        int diff = lenA - lenB;
        ListNode head1=new ListNode();
        ListNode head2=new ListNode();
        if (diff>=0){
            head1.next = headA;
            head2.next = headB;

        }
        else{
            diff = - diff;
            head1.next = headB;
            head2.next = headA;
        }

        for(int i=0;i<diff;++i){
            head1 = head1.next;
        }

        

        while(head1.next!=null && head2.next!=null){
            if (head1.next == head2.next){
                return head2.next;
            }
            head1 = head1.next;
            head2 = head2.next;
        }
        return null;
        
    }
    public int getListLen(ListNode node){
        int len = 0;
        while (node!=null){
            len += 1;
            node = node.next;
        }
        return len;

    }
}
