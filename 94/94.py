# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) :
        if not root:
            return []
        layers = [[root,0]]
        res = []
        while len(layers) != 0:
            
            curNode = layers[-1][0]
            stage = layers[-1][1]
            if stage == 0:
                if curNode.left != None:
                    layers.append([curNode.left,0])
                    layers[-2][1] = 1 # append 一项，所以下表变为 -2
                    continue
                layers[-1][1] = 1

            elif stage == 1:
                res.append(curNode.val)
                layers[-1][1] = 2
                
            elif stage == 2:
                layers.pop()
                if curNode.right != None:
                    layers.append([curNode.right,0])
            
        return res

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

s = Solution()
s.inorderTraversal(n1)