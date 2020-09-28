# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        pathp = []
        pathq = []
        tempPath = []
        
        
        def dfs(root,target,path):
            nonlocal flag
            if not root or flag == 1:
                return None
            path.append(root)
            if root.val == target:
                flag = 1
                nonlocal tempPath
                tempPath = path
                return None
            else:
                if target < root.val:
                    dfs(root.left,target,path+[root.left])
                else:
                    dfs(root.right,target,path+[root.right])
        flag = 0
        dfs(root,p.val,[])
        pathp = tempPath
        flag = 0
        dfs(root,q.val,[])
        pathq = tempPath

        i = 0
        while i<len(pathp) and i<len(pathq):
            print(pathp[i].val , pathq[i].val)
            if pathp[i] != pathq[i]:
                return pathp[i-1]
            i += 1

        if len(pathq) < len(pathp):
            return pathq[-1]
        else:
            return pathp[-1]
