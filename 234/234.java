
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head.next == null){
            return true;
        }
        ListNode slow=head,fast=head,pre=null,nextSlow=null;
        while(true){
            if(fast.next!=null){
                if(fast.next.next!=null){
                    fast = fast.next.next;
                    nextSlow = slow.next;
                    slow.next = pre;
                    pre = slow;
                    slow = nextSlow;
                }
                else{
                    // fast 的下下一跳是 null，说明链表长度为偶数，slow 所在的位置是前半段链表的起点
                    fast = slow.next;
                    slow.next = pre;
                    break;
                }
            }
            else{
                // fast 的下一跳就是 null，说明链表长度为奇数，slow 所在的位置就是链表的中间
                fast = slow.next;
                slow = pre;

                break;
            }
        }
        while(fast!=null && slow!=null){
            if(fast.val!=slow.val){
                return false;
            }
            fast = fast.next;
            slow = slow.next;

        }
        return true;
    }
}