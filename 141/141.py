# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        cur = head
        while cur != None:
            visited.add(cur)
            cur = cur.next
            if cur in visited:
                return True
        return False
