# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        path = []
        def mlr(root):
            if not root:
                return None
            nonlocal path
            path.append(root.val)
            mlr(root.left)
            mlr(root.right)
        mlr(root)
        return path
