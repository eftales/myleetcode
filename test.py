class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)

t1.left = t3
t3.right = t2

aa = [(1,1),(2,2)]
for x,y in aa:
    print(x,y)


a = set()
a.add(1)
b = set()
b.add(2)
c = set.union(a,b)
print(a.union(b))
print(a)