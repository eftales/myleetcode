class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def dfs(root,childType): # childType=1 -> leftChild childType=2-> rightChild
            if root.left == None and root.right == None:
                if childType == 1:
                    return root.val
                else:
                    return 0
            
            res = 0
            if root.left != None:
                res += dfs(root.left,1)
            if root.right != None:
                res += dfs(root.right,2)
            return res
        
        if not root:
            return 0
        return dfs(root,2)