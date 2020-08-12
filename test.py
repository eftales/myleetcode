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


class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

l = [1,2,3,4]
n1 = Node(1,l)
n2 = Node(2,l)
nl = (n1,n2)
print(nl[0].neighbors,nl[1].neighbors,l)
def t22(nodeList):
    nodeList[0].neighbors.pop()
t22(nl)
print(nl[0].neighbors,nl[1].neighbors,l)
print(l)

print("---------")
n1 = Node(1,l.copy())
n2 = Node(2,l.copy())
nl = (n1,n2)
print(nl[0].neighbors,nl[1].neighbors,l)
def t22(nodeList):
    nodeList[0].neighbors.pop()
t22(nl)
print(nl[0].neighbors,nl[1].neighbors,l)
print(l)