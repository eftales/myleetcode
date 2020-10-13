# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        curMin = None
        before = None
        def dfs(root):
            nonlocal curMin,before
            if root.left != None:
                dfs(root.left)
            if curMin == None and before != None:
                curMin = root.val - before
            elif curMin != None and before != None:
                curMin = curMin if curMin < (root.val - before) else (root.val - before)
            before = root.val
            if root.right != None:
                dfs(root.right)
        dfs(root)
        return curMin
        