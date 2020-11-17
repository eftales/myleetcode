import heapq
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        nodes = []
        for i in range(0,R):
            for j in range(0,C):
                dis = abs(i-r0) + abs(j-c0)
                heapq.heappush(nodes,[dis,(i,j)])
        
        res = []
        while len(nodes) != 0:
            res.append(heapq.heappop(nodes)[1])
        return res

