class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while True:
            if fast.next != None:
                fast = fast.next
                slow = slow.next
            if fast.next != None:
                fast = fast.next
            else:
                break
        return slow