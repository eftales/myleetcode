# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        myHead = ListNode(None,head)
        left = myHead
        flag = False
        while left != None:
            mid = left.next
            if not mid:
                break
            right = mid.next
            if not right:
                break
            if flag == False:
                head = right
                flag = True
            left.next = right
            mid.next = right.next
            right.next = mid
            left = mid
        return head
        