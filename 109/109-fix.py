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
        length = 0
        while cur != None:
            length += 1
            cur = cur.next
        cur = head

        def buildFullyBalancedBinaryTree(n:int):
            nonlocal cur
            if n == 0:
                return None
            rightNum = (n-1) //2
            leftNum = n - 1 - rightNum
            leftTree = None
            if leftNum > 1:
                leftTree = buildFullyBalancedBinaryTree(leftNum)
            elif leftNum == 1:
                leftTree = TreeNode(cur.val)
                cur = cur.next
            
            curRoot = TreeNode(cur.val) # 中序
            cur = cur.next

            rightTree = None
            if rightNum > 1:
                rightTree = buildFullyBalancedBinaryTree(rightNum)
            elif rightNum == 1:
                rightTree = TreeNode(cur.val)
                cur = cur.next

            curRoot.left = leftTree
            curRoot.right = rightTree

            return curRoot
        
        treeRoot = buildFullyBalancedBinaryTree(length)
        

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
