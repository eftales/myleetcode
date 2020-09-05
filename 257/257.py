class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = [ ]
        def dfs(root:TreeNode,path:list):
                path.append(root.val)
                if root.left == None and root.right == None:
                    res.append("->".join(map(str,path)))
                if root.left != None:
                    dfs(root.left,path)
                if root.right != None:
                    dfs(root.right,path)
                path.pop()
        
        dfs(root,[])
        return res