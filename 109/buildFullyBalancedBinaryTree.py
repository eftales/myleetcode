class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildFullyBalancedBinaryTree(n:int):
    if n == 0:
        return None
    rightNum = (n-1) //2
    leftNum = n - 1 - rightNum
    leftTree = None
    if leftNum > 1:
        leftTree = buildFullyBalancedBinaryTree(leftNum)
    elif leftNum == 1:
        leftTree = TreeNode()
    rightTree = None
    if rightNum > 1:
        rightTree = buildFullyBalancedBinaryTree(rightNum)
    elif rightNum == 1:
        rightTree = TreeNode()

    
    curRoot = TreeNode()
    curRoot.left = leftTree
    curRoot.right = rightTree

    return curRoot

tt = buildFullyBalancedBinaryTree(5)
l = 1