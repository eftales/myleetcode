class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def generateNodeList(nodeVal):
    res = ListNode(0)
    cur = res
    for val in nodeVal:
        cur.next = ListNode(val)
        cur = cur.next
    return res.next




nl = generateNodeList([4,19,14,5,-3,1,8,5,11,15])
