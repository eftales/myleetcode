class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = dict()
        outdegree = dict()

        for i in range(0,numCourses):
            indegree[i] = 0
            outdegree[i] = []

        for each in prerequisites:
            indegree[each[1]] += 1
            outdegree[each[0]].append(each[1])

        indegree0 = []
        for each in indegree:
            if indegree[each] == 0:
                indegree0.append(each)
        
        for each in indegree0:
                indegree.pop(each)

        while len(indegree0)!=0:
            curIndegree0 = indegree0.pop()

            for each in outdegree[curIndegree0]:
                indegree[each] -= 1
                if indegree[each] == 0:
                    indegree0.append(each)
                    indegree.pop(each)
        
        if len(indegree)!=0:
            return False

        return True

s = Solution()
s.canFinish(2,[[1,0],[0,1]])