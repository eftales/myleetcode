# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def getGrandChild(node):
            if not node:
                return False
            child = node.next
            if not child:
                return False
            grandChild = child.next
            if not grandChild:
                return False
            return grandChild
            

        if not getGrandChild(head):
            return None
        slow = head.next
        fast = slow.next
        
        while slow != fast:
            fast = getGrandChild(fast)
            if not fast:
                return None
            
            slow = slow.next

        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next
        return ptr
