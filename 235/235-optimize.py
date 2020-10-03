class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root,target1,target2):
            if not root:
                return None
            res = None
            if root.val > target1 and root.val > target2:
                res = dfs(root.left,target1,target2)
            elif root.val < target1 and root.val < target2:
                res = dfs(root.right,target1,target2)
            elif target1 < root.val < target2:
                res = root
            elif target1 == root.val or target2 == root.val:
                res = root
            return res
        if p.val < q.val:
            return dfs(root,p.val,q.val)
        else:
            return dfs(root,q.val,p.val)


