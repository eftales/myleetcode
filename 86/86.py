# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smallChainHead = ListNode(0)
        small = smallChainHead
        bigChainHead = ListNode(0)
        big = bigChainHead

        while head != None:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        small.next = bigChainHead.next
        big.next = None # 精华
        return smallChainHead.next



def generateNodeList(nodeVal):
    res = ListNode(0)
    cur = res
    for val in nodeVal:
        cur.next = ListNode(val)
        cur = cur.next
    return res.next




s = Solution()
s.partition(generateNodeList([1,4,3,2,5,2]),3)
