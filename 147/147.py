# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head) :
        if not head:
            return None
        sortedHead = head
        
        cur = head.next
        sortedHead.next = None
        
        while cur != None:
            loc = sortedHead
            nextCur = cur.next
            cur.next = None
            while loc != None:
                if cur.val >= loc.val:
                    if loc.next == None:
                        loc.next = cur
                        break
                    elif loc.next.val >= cur.val:
                        cur.next = loc.next
                        loc.next = cur
                        break
                    else:
                        loc = loc.next
                else:
                    cur.next = sortedHead
                    sortedHead = cur
                    break
            cur = nextCur
        return sortedHead



def generateNodeList(nodeVal):
    res = ListNode(0)
    cur = res
    for val in nodeVal:
        cur.next = ListNode(val)
        cur = cur.next
    return res.next

s = Solution()
s.insertionSortList(generateNodeList([4,19,14,5,-3,1,8,5,11,15]))
