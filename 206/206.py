class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        left = None
        mid = head
        right = mid.next

        while mid != None:
            right = mid.next # high light
            mid.next = left
            left = mid
            mid = right

        return left