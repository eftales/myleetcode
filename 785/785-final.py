class Solution:
    def isBipartite(self, graph) -> bool:
        partA = set()
        partB = set()
        allPoints = set(range(0,len(graph)))
        nextPoint = list()
        
        nextPoint.append(0)
        while (len(nextPoint)!=0):
            pointID = nextPoint.pop()
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
                elif eachPoint in otherPart:
                    continue
                otherPart.add(eachPoint)
                nextPoint.append(eachPoint)

            if len(nextPoint) == 0: # 非强连通图需要手动安排下一个点
                    nextPoint = list(allPoints - partA - partB)
                    continue
        return True


s = Solution()
print(s.isBipartite([[],[3],[],[1],[]]))
print(s.isBipartite( [[1,3], [0,2], [1,3], [0,2]]))
print(s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
print(s.isBipartite( [[1],[0,3],[3],[1,2]] ))
print(s.isBipartite( [[3],[2,4],[1],[0,4],[1,3]]))
print(s.isBipartite( [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]))

