# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) :
        layers = []
        res = []
        while root or len(layers) != 0:
            while root:
                layers.append(root)
                root = root.left

            root = layers.pop()
            res.append(root.val)
            root = root.right


        return res

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

s = Solution()
s.inorderTraversal(n1)