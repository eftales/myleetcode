import heapq
class Solution:
    def topKFrequent(self, nums, k: int) :
        count = dict()
        for each in nums:
            if each in count:
                count[each] += 1
            else:
                count[each] = 1
        
        res = []
        for each in count:
            if len(res) < k:
                heapq.heappush(res,[count[each],each])
            else:
                if count[res[0][1]] < count[each]:
                    heapq.heappop(res)
                    heapq.heappush(res,[count[each],each])
        for i in range(0,k):
            res[i] = res[i][1]
        return res

s = Solution()
s.topKFrequent([4,1,-1,2,-1,2,3],
2)