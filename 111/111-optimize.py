# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root) -> int:        
        if root == None:
            return 0

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        if rightDepth == 0 or leftDepth == 0: # 等于零说明缺失一个子树
            return max(leftDepth,rightDepth)+1
        else:
            return min(rightDepth,leftDepth)+1
    

