# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        cur = head
        pre = None
        length = 0
        while cur != None:
            length += 1
            cur.previous = pre
            pre = cur
            cur = cur.next
        
        listMid = head
        listMidIndex = length // 2
        for i in range(0,listMidIndex):
            listMid = listMid.next
        
        treeRoot = TreeNode(listMid.val)

        leftTree = treeRoot
        pre = listMid.previous
        while pre != None:
            leftTree.left = TreeNode(pre.val)
            pre = pre.previous
            leftTree = leftTree.left

        rightTree = treeRoot
        nxt = listMid.next
        while nxt != None:
            rightTree.right = TreeNode(nxt.val)
            nxt = nxt.next
            rightTree = rightTree.right

        return treeRoot     

l10 = ListNode(-10)
l3 = ListNode(-3)
l0 = ListNode(0)
l5 = ListNode(5)
l9 = ListNode(9)
l10.next = l3
l3.next = l0
l0.next = l5
l5.next = l9

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l0.next = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5


s = Solution()
s.sortedListToBST(l0)
