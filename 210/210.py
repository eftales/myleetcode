class Solution:
    def findOrder(self, numCourses, prerequisites) :
        indegree = dict() # 用于记录所有点的入度值
        outdegree = dict()
        res = []

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
                res.insert(0,each)

        # 删掉入度值为 0 的点
        for each in indegree0:
                indegree.pop(each)

        while len(indegree0)!=0:
            curIndegree0 = indegree0.pop()

            for each in outdegree[curIndegree0]:
                indegree[each] -= 1
                if indegree[each] == 0:
                    res.insert(0,each)
                    indegree0.append(each)
                    indegree.pop(each)
        
        # 判断记录入度值的点的数据结构内部是否还有元素，有说明成环了
        if len(indegree)!=0:
            return []

        return res



s = Solution()
print(s.findOrder(2, [[1,0]]))
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))