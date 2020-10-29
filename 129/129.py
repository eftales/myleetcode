# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import reduce
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        path = []
        nums = []
        def dfs(root):
            if not root:
                return 
            nonlocal path,nums
            path.append(root.val)
            if root.left == None and root.right == None:
                nums.append(reduce(lambda x,y: x*10+y,path))
            else:
                dfs(root.left)
                dfs(root.right)
            path.pop(-1)
        
        dfs(root)
        return sum(nums)