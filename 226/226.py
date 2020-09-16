class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def inverse(root):
            if not root:
                return None
            
            inverse(root.left)
            inverse(root.right)
            root.left,root.right = root.right,root.left
        
        inverse(root)
        return root