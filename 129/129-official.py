class Solution:
    def sumNumbers(self, root) -> int:
        def dfs(root,preVal):
            if not root:
                return 0
            newVal = preVal * 10 + root.val
            if root.left == None and root.right == None:
                return newVal
            else:
                return dfs(root.left,newVal) + dfs(root.right,newVal)
        
        return dfs(root,0)