# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) :
        from copy import deepcopy
        f = [ [] for i in range(0,n+1) ]
        f[0].append(None)
        if n == 0:
            return []
        node1 = TreeNode(1)
        node1.left = None
        node1.right = None
        f[1].append(node1)

        def combine(f,root,left,right):
            newTrees = []
            for leftTree in f[len(left)]:
                for rightTree in f[len(right)]:
                    newTree = TreeNode(root)
                    '''
                    # 错误示范，直接赋值只是把引用赋值给了 left，一个 newTree 更改了其 leftTree 的 val 属性，会影响到其他 newTree 的 leftTree 属性
                    newTree.left = leftTree
                    newTree.right = rightTree
                    '''
                    newTree.left = deepcopy(leftTree)
                    newTree.right = deepcopy(rightTree)
                    newTrees.append(newTree)
            return  newTrees

        def frontRoot(n,root):
            if root.left != None: # 先序遍历的逻辑：如果有 X 子树，就遍历，没有就算了
                n,leftChild = frontRoot(n,root.left)
                n += 1
                root.left = leftChild
            
            
            root.val = n

            if root.right != None: # 右子树就不需要特殊的判断了
                n,rightChild = frontRoot(n+1,root.right)
                root.right = rightChild

            return n,root



        for i in range(2,n+1):
            for j in range(1,i+1):
                left = list(range(1,j))
                right = list(range(j+1,i+1))
                f[i] += combine(f,j,left,right)

        for i in range(0,len(f[n])):
            _,f[n][i] = frontRoot(1,f[n][i])
        return f[n]



s = Solution()
print(s.generateTrees(4))
