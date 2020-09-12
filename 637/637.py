# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        layers = []
        def dfs(root,n):
            if not root:
                return None
            if n >= len(layers):
                layers.append([])
            layers[n].append(root.val)
            dfs(root.left,n+1)
            dfs(root.right,n+1)
        dfs(root,0)
        res = []
        for each in layers:
            res.append(sum(each)/len(each))
        return res
