# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def lrm(root):
            if not root:
                return None
            nonlocal res
            lrm(root.left)
            lrm(root.right)
            res.append(root.val)
        lrm(root)
        return res