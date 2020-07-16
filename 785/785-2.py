class Solution:
    def isBipartite(self, graph) -> bool:
        partA = set()
        partB = set()

        for pointID in range(0,len(graph)):
            myPart = None
            otherPart = None
            for eachPoint in graph[pointID]:
                if myPart == None:
                    if eachPoint in partA:
                        myPart = partB
                        otherPart = partA
                    elif eachPoint in partB:
                        myPart = partA
                        otherPart = partB
                    if myPart != None:
                        myPart.add(pointID)
                        break
            else: # 只要 for 循环没有被 break 掉，就会执行 else 语句
                myPart = partA
                otherPart = partB
                myPart.add(pointID)

            for eachPoint in graph[pointID]:
                if eachPoint in myPart:
                    return False
                otherPart.add(eachPoint)
                
        return True


s = Solution()

print(s.isBipartite( [[3],[2,4],[1],[0,4],[1,3]]))
