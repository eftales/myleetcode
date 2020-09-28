# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        counts = dict()
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            dfs(root.right)
            if root.val in counts:
                counts[root.val] += 1
            else:
                counts[root.val] = 1

        dfs(root)
        res = []
        print(counts)
        for eachKey in counts:
            if not res:
                res.append(eachKey)
            else:
                if counts[eachKey] > counts[res[0]]:
                    res = [eachKey]
                elif counts[eachKey] == counts[res[0]]:
                    res.append(eachKey)
        return res
            
