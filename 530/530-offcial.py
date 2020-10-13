# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(root,curMin,preVal):
            if root.left != None:
                [curMin,preVal] = dfs(root.left,curMin,preVal)
            if curMin == None and preVal != None:
                curMin = root.val - preVal
            elif curMin != None and preVal != None:
                curMin = curMin if curMin < (root.val - preVal) else (root.val - preVal)
            preVal = root.val
            if root.right != None:
                [curMin,preVal] = dfs(root.right,curMin,preVal)
            
            return [curMin,preVal]
        [curMin,preVal] = dfs(root,None,None)
        return curMin


s = Solution()
n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(7)
n1.left = n2
n1.right = n3
s.getMinimumDifference(n1)