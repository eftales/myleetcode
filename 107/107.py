class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:  
        res = []
        def bfs(Cqueue):
            Nqueue = []
            res.insert(0,[])
            for eachNode in Cqueue:
                if eachNode:
                    res[0].append(eachNode.val)
                    Nqueue.append(eachNode.left)
                    Nqueue.append(eachNode.right)
            return Nqueue
        
        Cqueue = [root]
        while len(Cqueue) != 0:
            Cqueue = bfs(Cqueue)
        
        res.pop(0)
        return res
