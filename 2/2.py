# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        head = res
        while l1 != None or l2 != None:
            l1Val = 0 if l1 == None else l1.val
            l2Val = 0 if l2 == None else l2.val

            res.val = l1Val + l2Val + res.val
            res.next = ListNode(res.val//10)
            res.val = res.val % 10

            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next
            if l1 == None and l2 == None:
                if res.next.val == 0:
                    res.next = None
                return head
            res = res.next

            