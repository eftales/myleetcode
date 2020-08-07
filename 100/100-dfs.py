# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p == None and q == None: # 两个都是 None
            return True
        elif p == None or q == None: # 两个里面有一个是 None
            return False
        else:
            # 两个都不是 None
            if p.val != q.val: # 发现节点的 val 不一样
                return False
            else:
                # 还需要进一步判断左右子树，一旦发现一次  False，就会把 False 一层一层 return 回去
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            



        
