class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        if node == None:
            return Node

        def cloneNode(node):
            newNode = Node(node.val,[])
            return newNode

        newNodes = dict()
        newRootNode = cloneNode(node)
        newNodes[newRootNode.val] = newRootNode

        tobevisit = []
        tobevisit.append(node)

        while len(tobevisit) != 0:
            curOldNode = tobevisit.pop()
            for eachOldNeighbor in curOldNode.neighbors:
                if eachOldNeighbor.val not in newNodes:
                    tobevisit.append(eachOldNeighbor)
                    newNeighbor = cloneNode(eachOldNeighbor)
                    newNodes[newNeighbor.val] = newNeighbor
                    newNodes[curOldNode.val].neighbors.append(newNeighbor)
                else:
                    newNodes[curOldNode.val].neighbors.append(newNodes[eachOldNeighbor.val])
        return newNodes[node.val]


s = Solution()
# 这样创建 Node 存在风险，解决方法可见 ../Python语言特性/类构造函数的默认参数.md
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors = [n2,n4]
n2.neighbors = [n1,n3]
n3.neighbors = [n2,n4]
n4.neighbors = [n1,n3]

d = s.cloneGraph(n1)
i = 10