class Solution:
    def isBipartite(self, graph) -> bool:
        partA = set()
        partB = set()

        for pointID in range(0,len(graph)):
            if pointID not in partB:
                myPart = partA
                otherPart = partB

            else:
                myPart = partB
                otherPart = partA
            
            myPart.add(pointID)
            for eachPoint in graph[pointID]:
                if eachPoint in myPart:
                    return False
                otherPart.add(eachPoint)
        return True


s = Solution()
print(s.isBipartite( [[1],[0,3],[3],[1,2]] ))
