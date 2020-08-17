class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def dfs(root):
            lenl = 0
            lenr = 0
            if root.left != None:
                lenl = dfs(root.left)
            
            if root.right != None:
                lenr = dfs(root.right)

            if lenl is False or lenr is False or abs(lenl-lenr)>1:
                return False
            else:
                return max(lenl,lenr)+1
        res = dfs(root)
        if res != False:
            res = True
        return res

n3 = TreeNode(3)
n9 = TreeNode(9)
n20 = TreeNode(20)
n15 = TreeNode(15)
n7 = TreeNode(7)

n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7

s = Solution()
s.isBalanced(n3)