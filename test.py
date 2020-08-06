class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t = TreeNode(1)

t.pp = 22

print(hasattr(t,"pp"))
