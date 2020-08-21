# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        
        def dfs(root):
            leftDepth = 0
            if root.left != None:
                leftDepth = dfs(root.left)
            
            rightDepth = 0
            if root.right != None:
                rightDepth = dfs(root.right)
            
            if rightDepth == 0 or leftDepth == 0: # 等于零说明缺失一个子树
                return max(leftDepth,rightDepth)+1
            else:
                return min(rightDepth,leftDepth)+1
        
        
        return dfs(root)
