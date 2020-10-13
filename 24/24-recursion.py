class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head != None and head.next!=None:
            second = head.next
            head.next = self.swapPairs(second.next)
            second.next = head
            head = second
            
        return head
        