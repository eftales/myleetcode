class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recursion(head):
            if not head or not head.next:
                return head
            newHead = recursion(head.next)
            head.next.next = head
            head.next = None
            return newHead
        return recursion(head)