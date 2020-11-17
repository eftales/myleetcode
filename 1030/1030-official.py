class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) :
        maxManhatun = max(r0,R-1-r0) + max(c0,C-1-c0)
        bucket = [[] for i in range(maxManhatun+1)] # 设置 defaultdict

        for i in range(0,R):
            for j in range(0,C):
                dis = abs(i-r0) + abs(j-c0)
                bucket[dis].append((i,j))
        
        res = []
        for i in range(0,maxManhatun+1):
            res += bucket[i]

        return res

